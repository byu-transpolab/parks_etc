import shapefile
from json import dumps
import osmnx as ox
%matplotlib inline
ox.config(log_console=True, use_cache=True)
ox.__version__

place = 'Piedmont, California, USA'
gdf = ox.gdf_from_place(place)
gdf.loc[0, 'geometry']
ox.save_gdf_shapefile(gdf, filename='place-shape2', folder='data')

# read the shapefile
reader = shapefile.Reader("data/place-shape2/place-shape2.shp")
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", \
     geometry=geom, properties=atr))
# write the GeoJSON file

geojson = open("pyshp-demo.json", "w")
geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
geojson.close()

import shapefile
from json import dumps

# read the shapefile
reader = shapefile.Reader("data/the-place/nodes/nodes.shp")
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", \
     geometry=geom, properties=atr))
# write the GeoJSON file

geojson = open("nodes.json", "w")
geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
geojson.close()

print('hi')
################################################################################
# read the shapefile
reader = shapefile.Reader("data/the-place/edges/edges.shp")
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", \
     geometry=geom, properties=atr))
# write the GeoJSON file

geojson = open("edges.json", "w")
geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
geojson.close()

print('hi hi')

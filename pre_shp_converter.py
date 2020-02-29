
import osmnx as ox
%matplotlib inline
ox.config(log_console=True, use_cache=True)
ox.__version__

##Area by lat/long points listed below:
north, south, east, west = 40.0680, 40.0135, -111.7046, -111.7771


'''
place = 'Payson, Utah, USA'
gdf = ox.gdf_from_place(place)
#gdf.loc[0, 'geometry']
ox.save_gdf_shapefile(gdf, filename='place-shape2', folder='data')'''

print('hi')

B = ox.graph_from_bbox(north, south, east, west, network_type='drive')
ox.save_graph_shapefile(B, filename='the-place', folder='data')

print('hi hi')
'''B = ox.graph_from_bbox(north, south, east, west, network_type='drive')
gdf_nodes, gdf_edges = ox.graph_to_gdfs(
        B,
        nodes=True, edges=True,
        node_geometry=True,
        fill_edge_geometry=True)

ox.save_gdf_shapefile(gdf_nodes, filename='the_places_nodes', folder='data')
ox.save_gdf_shapefile(gdf_edges, filename='the_places_edges', folder='data')
'''
'''
north, south, east, west = 40.0680, 40.0135, -111.7046, -111.7771
gdf = ox.gdf_from_bbox(north, south, east, west, network_type='drive')
gdf.loc[0, 'geometry']
ox.save_gdf_shapefile(gdf, filename='place-shape3', folder='data')
print('why hello')'''




'''
n, s, e, w = 40.0680, 40.0135, -111.7046, -111.7771
gdf = ox.create_footprints_gdf(polygon=None, north=n, south=s, east=e, west=w, footprint_type='building', retain_invalid=False, responses=None)

ox.save_gdf_shapefile(gdf, filename='footprint_test', folder='data')

ox.plot_footprints(gdf, fig=None, ax=None, figsize=None, color='#333333', bgcolor='w', set_bounds=True, bbox=None, save=False, show=True, close=False, filename='image', file_format='png', dpi=600)
'''

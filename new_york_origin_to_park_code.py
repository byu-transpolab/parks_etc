import osmnx as ox
%matplotlib inline
import networkx as nx
B = ox.graph_from_point((40.73077, -73.935076), distance=2000, network_type='drive')
#the above is calvary cemetary at NeW York, New York

##read in the file of lat/long points
##store origin values of lat. as xstart, and long. as ystart
##store destination values of lat. as xend, and long. as yend

##create a forloop here, for (length of xstart)
## next steps (tbd)...
origin = ox.get_nearest_node(B, (xstart, ystart)) #can use (40.738543, -73.926721) as an example
destination = ox.get_nearest_node(B, (xend, yend)) #can use (40.725564, -73.942889) as an example
bbox = ox.bbox_from_point((40.73077, -73.935076), distance=2000, project_utm=True)
#this lat/long needs to be the same value as map "B" notated above

B_proj = ox.project_graph(B)
route = nx.shortest_path(B_proj, source=origin, target=destination, weight='length')
fig, ax = ox.plot_graph_route(B_proj, route, bbox=bbox, node_size=0)

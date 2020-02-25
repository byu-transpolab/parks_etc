import osmnx as ox
%matplotlib inline
import networkx as nx
import pandas as pd
import io
import requests




##below is uploading the NY data
################################################################

url = "https://www2.census.gov/geo/docs/reference/cenpop2010/blkgrp/CenPop2010_Mean_BG36.txt"
c = pd.read_csv(url)
c['COUNTYFP'] = c['COUNTYFP'].apply('{0:0>3}'.format)
c['TRACTCE'] = c['TRACTCE'].apply('{0:0>6}'.format)
c = c.astype(str)
c['POPULATION'] = c['STATEFP'] + c['COUNTYFP'] + c['TRACTCE'] + c['BLKGRPCE']
c.rename(columns = {'POPULATION':'BLOCKNUMBER'}, inplace=True)
c=c.drop('COUNTYFP',axis = 1)
c=c.drop('STATEFP',axis = 1)
c=c.drop('TRACTCE',axis = 1)
c=c.drop('BLKGRPCE',axis = 1)
c['LATITUDE'] = c['LATITUDE'].astype(float)
c['LONGITUDE'] = c['LONGITUDE'].astype(float)



print(c)

c2 = c[['LATITUDE','LONGITUDE']]
c3 = c2[1:4]
print(c3)

xstart = c3.iat[0,0]
ystart = c3.iat[0,1]
B = ox.graph_from_point((xstart, ystart), distance=2000, network_type='drive')
#origin = ox.get_nearest_node(B, (xstart, ystart))
#destination = ox.get_nearest_node(B, (xend, yend))

fig, ax = ox.plot_graph(ox.project_graph(B))
##notice this above destination is not in New York City... 


'''
##below is the code to start calculating distance between points
################################################################
B = ox.graph_from_point((40.73077, -73.935076), distance=2000, network_type='drive')
##the above is calvary cemetary at NeW York, New York
##For the real simulation, load "B" as the entire city of New York.
##This will be this below code:
#B = ox.graph_from_place('New York, New York, USA', network_type='drive')

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
'''

import osmnx as ox
%matplotlib inline
import networkx as nx

import numpy as np
import pandas as pd
import io
import requests

url = "https://www2.census.gov/geo/docs/reference/cenpop2010/blkgrp/CenPop2010_Mean_BG36.txt"
c = pd.read_csv(url)
c['COUNTYFP'] = c['COUNTYFP'].apply('{0:0>3}'.format)
c['TRACTCE'] = c['TRACTCE'].apply('{0:0>6}'.format)
length = c.shape[0]
county081 = c.query('COUNTYFP == "081"').index
print(county081[1745])
county047 = c.query('COUNTYFP == "047"').index
county061 = c.query('COUNTYFP == "061"').index
county005 = c.query('COUNTYFP == "005"').index
county085 = c.query('COUNTYFP == "085"').index
len81 = len(county081)-1
len47 = len(county047)-1
len61 = len(county061)-1
len5 = len(county005)-1
len85 = len(county085)-1


hh = pd.DataFrame(columns=c.columns)
cond = c.COUNTYFP == '081'
rows = c.loc[cond, :]
hh = hh.append(rows, ignore_index=True)
c.drop(rows.index, inplace=True)

jj = pd.DataFrame(columns=c.columns)
cond = c.COUNTYFP == '047'
rows = c.loc[cond, :]
jj = jj.append(rows, ignore_index=True)
c.drop(rows.index, inplace=True)

kk = pd.DataFrame(columns=c.columns)
cond = c.COUNTYFP == '061'
rows = c.loc[cond, :]
kk = kk.append(rows, ignore_index=True)
c.drop(rows.index, inplace=True)

mm = pd.DataFrame(columns=c.columns)
cond = c.COUNTYFP == '005'
rows = c.loc[cond, :]
mm = mm.append(rows, ignore_index=True)
c.drop(rows.index, inplace=True)

nn = pd.DataFrame(columns=c.columns)
cond = c.COUNTYFP == '085'
rows = c.loc[cond, :]
nn = nn.append(rows, ignore_index=True)
c.drop(rows.index, inplace=True)


frames = [hh, jj, kk, mm, nn]
result = pd.concat(frames)
print(result)


result = result.astype(str)
result['POPULATION'] = result['STATEFP'] + result['COUNTYFP'] + result['TRACTCE'] + result['BLKGRPCE']
result.rename(columns = {'POPULATION':'BLOCKNUMBER'}, inplace=True)
result=result.drop('COUNTYFP',axis = 1)
result=result.drop('STATEFP',axis = 1)
result=result.drop('TRACTCE',axis = 1)
result=result.drop('BLKGRPCE',axis = 1)
result['LATITUDE'] = result['LATITUDE'].astype(float)
result['LONGITUDE'] = result['LONGITUDE'].astype(float)




print(result)
print('\n')
print(result.shape[0])


'''
##block time
############################################################
xstart = result.iat[500,1]
ystart = result.iat[500,2]
B = ox.graph_from_place('New York, New York, USA', network_type='drive')
#B = ox.graph_from_point((xstart, ystart), distance=2000, network_type='drive')
origin = ox.get_nearest_node(B, (xstart, ystart))
xend = 40.731456
yend = -73.770367
destination = ox.get_nearest_node(B, (xend, yend))

bbox = ox.bbox_from_point((xend, yend), distance=500, project_utm=True)
#this lat/long needs to be the same value as map "B" notated above
B_proj = ox.project_graph(B)
route = nx.shortest_path(B_proj, source=origin, target=destination, weight='length')
fig, ax = ox.plot_graph_route(B_proj, route, bbox=bbox, node_size=0)
#fig, ax = ox.plot_graph(ox.project_graph(B))

route_lengths = ox.get_route_edge_attributes(B_proj, route, 'length')
print('Total trip distance: {:,.0f} meters'.format(np.sum(route_lengths)))
gg = np.sum(route_lengths)
print(gg)
'''
B = ox.graph_from_place('New York, New York, USA', network_type='drive')
B_proj = ox.project_graph(B)


print('__________________________________________________________\n')
import pandas as pd
u = pd.read_csv('tester.csv')
print(u)
u['lat'] = u['lat'].astype(float)
u['long'] = u['long'].astype(float)


col_names = []

for name in range(0,5):
    b = result.iat[name,0]
    col_names.append(b)

rows = []
#rows.append(u.iat[0,0])
for parkid in range(0,3):
    f = u.iat[parkid,0]
    rows.append(f)

print('\n')
treasure = pd.DataFrame(index=rows,columns=col_names)

###now start calculating distances in a forloop!

total_rows = treasure.shape[0]
#total_rows = total_rows-1
total_columns = len(treasure.columns)

for tt in range(0,total_columns):
    #treasure.iat[tt,0] = 5
    for ii in range(0,total_rows):
        xstart = result.iat[tt,1]
        ystart = result.iat[tt,2]
        origin = ox.get_nearest_node(B, (xstart, ystart))
        xend = u.iat[ii,1]
        yend = u.iat[ii,2]
        destination = ox.get_nearest_node(B, (xend, yend))
        route = nx.shortest_path(B_proj, source=origin, target=destination, weight='length')
        route_lengths = ox.get_route_edge_attributes(B_proj, route, 'length')
        gg = np.sum(route_lengths)
        #print(gg)
        treasure.iat[ii,tt] = gg


print(treasure)

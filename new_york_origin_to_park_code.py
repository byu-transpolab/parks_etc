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
#print(county081[1745])
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
#print(result)


result = result.astype(str)
result['POPULATION'] = result['STATEFP'] + result['COUNTYFP'] + result['TRACTCE'] + result['BLKGRPCE']
result.rename(columns = {'POPULATION':'BLOCKNUMBER'}, inplace=True)
result=result.drop('COUNTYFP',axis = 1)
result=result.drop('STATEFP',axis = 1)
result=result.drop('TRACTCE',axis = 1)
result=result.drop('BLKGRPCE',axis = 1)
result['LATITUDE'] = result['LATITUDE'].astype(float)
result['LONGITUDE'] = result['LONGITUDE'].astype(float)




#print(result)
#print('\n')
#print(result.shape[0])
print('__________________________________________________________\n')
B = ox.graph_from_place('New York, New York, USA', network_type='drive')
B_proj = ox.project_graph(B)

u = pd.read_csv('the_data.csv')
#print(u)
u['latitude'] = u['latitude'].astype(float)
u['longitude'] = u['longitude'].astype(float)


col_names = []
qqq = result.shape[0]
for name in range(0,qqq):
    b = result.iat[name,0]
    col_names.append(b)

#print('length of result dataframe:')
#print(result.shape[0])


#x = 5
rows_in_park_IDs = u.shape[0]
park_IDs_orig = []
park_IDs_orig.append(u.iat[0,0])
#print(park_IDs_orig)
count = 0
for IDs in range(0,rows_in_park_IDs):
    if (park_IDs_orig[count] != u.iat[IDs,0]):
        count = count + 1
        park_IDs_orig.append(u.iat[IDs,0])

rows = []
for parkid in range(0,len(park_IDs_orig)):
    f = park_IDs_orig[parkid]
    rows.append(f)

print('\n')
treasure = pd.DataFrame(index=rows,columns=col_names)

###now start calculating distances in a forloop!

total_rows = treasure.shape[0]
#total_rows = total_rows-1
total_columns = len(treasure.columns)
#print(treasure)

for tt in range(0,total_columns):
    xstart = result.iat[tt,1]
    ystart = result.iat[tt,2]
    origin = ox.get_nearest_node(B, (xstart, ystart))
    xend = u.iat[0,1]
    yend = u.iat[0,2]
    destination = ox.get_nearest_node(B, (xend, yend))
    route = nx.shortest_path(B_proj, source=origin, target=destination, weight='length')
    route_lengths = ox.get_route_edge_attributes(B_proj, route, 'length')
    gg = np.sum(route_lengths)
    treasure.iat[0,tt] = gg


counter = 0
rowz = rows_in_park_IDs - 1


for jiber in range(1,rowz):
    if (u.iat[jiber,0] == u.iat[jiber-1,0]):
        for tt in range(0,total_columns):
            xstart = result.iat[tt,1]
            ystart = result.iat[tt,2]
            origin = ox.get_nearest_node(B, (xstart, ystart))
            xend = u.iat[jiber,1]
            yend = u.iat[jiber,2]
            destination = ox.get_nearest_node(B, (xend, yend))
            route = nx.shortest_path(B_proj, source=origin, target=destination, weight='length')
            route_lengths = ox.get_route_edge_attributes(B_proj, route, 'length')
            aa = np.sum(route_lengths)
            if (aa < treasure.iat[counter,tt]):
                treasure.iat[counter,tt] = aa
    else:
        counter = counter + 1
        for tt in range(0,total_columns):
            xstart = result.iat[tt,1]
            ystart = result.iat[tt,2]
            origin = ox.get_nearest_node(B, (xstart, ystart))
            xend = u.iat[jiber,1]
            yend = u.iat[jiber,2]
            destination = ox.get_nearest_node(B, (xend, yend))
            route = nx.shortest_path(B_proj, source=origin, target=destination, weight='length')
            route_lengths = ox.get_route_edge_attributes(B_proj, route, 'length')
            aa = np.sum(route_lengths)
            treasure.iat[counter,tt] = aa

#print(treasure)

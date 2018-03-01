# use ftp client to download all zip files from https://www2.census.gov/geo/tiger/TIGER2014/TRACT/
# unzip all to "*/" in tracts_path
import os
import geopandas as gpd
import time

start_time = time.time()
tracts_path = '2014-tracts-by-state'

gdf = gpd.GeoDataFrame()
for folder in os.listdir(tracts_path):
    print(folder)
    tmp = gpd.read_file('{}/{}'.format(tracts_path, folder))
    gdf = gdf.append(tmp)

gdf = gdf.head()

original_crs = tmp.crs
gdf.crs = original_crs
gdf = gdf.to_crs({'init' : 'epsg:4326'})
gdf.to_file('us_tracts_2014')

print('created shapefile with {} rows'.format(len(gdf)))
print('finished in {:.1f} seconds'.format(time.time()-start_time))

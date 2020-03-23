import pandas as pd
import geopandas as gpd
import os

os.chdir(r'C:\coronaMaps')
csv = r'https://disasterresponse.maps.arcgis.com/sharing/rest/content/items/6f3f214220f443b2beed8d1374b02cf7/data'
df = pd.read_csv(csv)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Long, df.Lat))
gdf.to_file("output.json", driver="GeoJSON")
import pandas as pd
import geopandas as gpd
import os
import numpy as np

# Grabbing data
os.chdir(r'C:\coronaMaps')
csv = r"C:\coronaMaps\johnHopRepo\COVID-19-master\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports\03-31-2020.csv"
df = pd.read_csv(csv)

# Cleaning Data
df = df[pd.notnull(df['Confirmed'])]
df = df[df['Lat'].abs() > 0.0]
df = df[df['Long_'].abs() > 0.0]

# Creating Death Rate Column
df['death_rate'] = df['Deaths']/df['Confirmed'] * 100
df['death_rate'] = df['death_rate'].round(2)
df['death_rate'][df['Confirmed'] < 200] = np.NaN

# Creating Recovery Rate Column
df['recovery_rate'] = df['Recovered']/df['Confirmed'] * 100
df['recovery_rate'] = df['recovery_rate'].round(2)
df['recovery_rate'][df['Confirmed'] < 200] = np.NaN

# Adding Geometry Column
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Long_, df.Lat))

# Exporting to GeoJSON
gdf.to_file("output.json", driver="GeoJSON")
#gdf.to_html('coronaTable.html')

# Creating Country Totals
result = df.groupby('Country_Region', as_index=False).agg({'Confirmed':'sum',
                   'Deaths': 'sum', 'Recovered': 'sum'})
result = result.sort_values('Confirmed', ascending=False).reset_index()
#result.to_html('maxTest.html')
result.to_json("maxTest.json")
'''
# Creating States GDF
statesJSON = gpd.read_file('states.json')
states = df.groupby('Province_State', as_index=False).agg({'Confirmed':'sum',
                   'Deaths': 'sum', 'Recovered': 'sum', 'Lat': 'mean', 'Long_': 'mean'})
states = gpd.GeoDataFrame(states, geometry=gpd.points_from_xy(states.Long_, states.Lat))
states.crs = {'init': 'epsg:4326', 'no_defs': True}
states = states.to_crs({'init': 'epsg:4326'})
statesGDF = gpd.sjoin(statesJSON, states, how='left', op='intersects')
statesGDF.to_file("usStatesCorona.json", driver="GeoJSON")
statesGDF.to_html('usstatestest.html')
'''
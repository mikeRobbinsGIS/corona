from __future__ import absolute_import, division, print_function
import pandas as pd

csv = r'https://disasterresponse.maps.arcgis.com/sharing/rest/content/items/6f3f214220f443b2beed8d1374b02cf7/data'
df = pd.read_csv(csv)

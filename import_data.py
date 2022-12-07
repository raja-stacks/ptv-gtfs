############################################################################
#
#     _|_|_|  _|_|_|_|_|  _|_|_|_|    _|_|_|
#   _|            _|      _|        _|
#   _|  _|_|      _|      _|_|_|      _|_|
#   _|    _|      _|      _|              _|
#     _|_|_|      _|      _|        _|_|_|
#
# Author: u/corkage_for_corkers
#
# Description: Manages API calls to PTV
#
############################################################################

# 00. Libraries, Parameters & Functions
import pandas as pd
import plotly as pl
import seaborn as sb

dataLocation = 'D:\\Projects\\ptv-gtfs\\data'

# Prepare mapping table for transport mode type (based on PTV release notes)
modeType = {
     'id': [1,2,3,4,5,6,7,8,10,11],
    'modeType': [
    'Regional Train',
    'Metropolitan Train',
    'Metropolitan Tram',
    'Metropolitan Bus',
    'Regional Coach',
    'Regional Bus',
    'TeleBus',
    'Night Bus',
    'Interstate',
    'Skybus'
    ]
 }

df_modeType = pd.DataFrame(
    modeType, columns = ['id', 'modeType']
)


# 01. Extract Data

# Initialise dicts
agency = {}
calendar =  {}
calendar_dates = {}
routes = {}
shapes = {}
stop_times = {}
stops = {}
trips = {}

# Populate dicts with data
for i in [1,2,3,4,5,6,7,8,10,11]:
    # Create dict names
    df_id = df_modeType[df_modeType['id'] == i]
    id = df_id.iloc[0]['id']
    modeType = df_id.iloc[0]['modeType']

    # Data location string
    dataLocationMode = dataLocation + '/' + str(id)
    print('i is ...' + '  ' + str(i))

    # Read data and assign to appropriate dict with mode information in datasets
    agency[str(id)] = pd.read_csv(dataLocationMode + '/' + 'agency.txt').assign(id = i, modeType = modeType)
    calendar[str(id)] = pd.read_csv(dataLocationMode + '/' + 'calendar.txt').assign(id = i, modeType = modeType)
    calendar_dates[str(id)] = pd.read_csv(dataLocationMode + '/' + 'calendar_dates.txt').assign(id = i, modeType = modeType)
    routes[str(id)] = pd.read_csv(dataLocationMode + '/' + 'routes.txt').assign(id = i, modeType = modeType)
    shapes[str(id)] = pd.read_csv(dataLocationMode + '/' + 'shapes.txt').assign(id = i, modeType = modeType)
    stop_times[str(id)] = pd.read_csv(dataLocationMode + '/' + 'stop_times.txt').assign(id = i, modeType = modeType)
    stops[str(id)] = pd.read_csv(dataLocationMode + '/' + 'stops.txt').assign(id = i, modeType = modeType)
    trips[str(id)] = pd.read_csv(dataLocationMode + '/' + 'trips.txt').assign(id = i, modeType = modeType)



###########################################
# 02. Wrangle Data
###########################################



###########################################
# 03. Plot Data
###########################################
import warnings; warnings.filterwarnings(action='ignore')
from matplotlib import pyplot as plt
import geopandas as gpd

shapes_shp = gpd.read_file('D:\\Projects\\ptv-gtfs\\data\\2\\ll_gda2020\\esrishape\\whole_of_dataset\\victoria\\PTV\\PTV_TRAIN_TRACK_CENTRELINE.shp')

shapes_upfield = shapes_shp.query('(FAC_NAME == "Southern Cross-Upfield") or (FAC_NAME == "North Melbourne-Upfield")')






############################## END OF PROGRAM ##############################



df_upfield = {}
df_upfield_routes = routes['2'][routes['2'].route_short_name == 'Upfield']
df_trips = trips['2']

df_upfield_joined = df_upfield_routes.merge(df_trips, on='route_id', how='left')
df_upfield_joined.to_csv('D:\\Projects\\ptv-gtfs\\data\\2\\df_upfield_joined.csv')















###########################################
# 00. Libraries & Parameters
###########################################
import pandas as pd
import numpy as np
import matplotlib as mp
import seaborn as sb
import requests as rq
import json

# Output location for data
dataLib = "C:/Users/Raja/Documents/projects/data"

# API URL
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes"

# Parameters for GET request that we will pass in
querystring = {"region":"US",
               "lang":"en",
               "symbols":"MSFT, AAPL, AMZN"}

# API tokens. The 'x-rapidapi-key' will need to be changed to your personal token
headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "5ad0a734c2msha4b7ed1d8eaa416p1b5daejsnf346dc1ba1d9"
    }

###########################################
# 01. Extract Data
###########################################
# GET Request to Yahoo Finance API
response = rq.request("GET", url, headers=headers, params=querystring)
dataText = response.text

if str(response) == "<Response [200]>":
    print("GET request successful...")

# $$$ - TBD Add certificate checking and handling

# Decode JSON data into a python dict object
with response.text as json_file:
    data = json.load(json_file)


from pandas.io.json import json_normalize

df = json_normalize(response, 'abc')
print (df)

###########################################
# 02. Wrangle Data
###########################################



###########################################
# 03. Plot Data
###########################################
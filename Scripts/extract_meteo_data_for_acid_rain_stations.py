# This script is for extracting meteorological data for each acid rain station
import xarray as  xr
import pandas as pd
import numpy as np
import os
os.chdir('/Users/zeqinhuang/Documents/paper/acid_rain')

variables = [
    '2m_dewpoint_temperature', 'boundary_layer_height', '2m_temperature', 'mean_sea_level_pressure', 'vertical_velocity_850hpa',
    'total_precipitation','total_cloud_cover','10m_v_component_of_wind','10m_u_component_of_wind','leaf_area_index_high_vegetation']

short_name = ['d2m','blh','t2m','msl','w', 'tp', 'tcc','v10','u10','lai_hv']

var_names = dict(zip(variables, short_name))
target_points = pd.read_csv('ACID_RAIN_DATA/acid_rain_station.csv',header=0,index_col=3)


for v in variables:
    v_df = pd.DataFrame()
    for index, row in target_points.iterrows():
        lon = int(row['Lon'])
        lat = int(row['LAT'])
        v_da = xr.open_dataarray('/Users/zeqinhuang/Documents/paper/acid_rain/ERA5_data/' + v + '_daily_era5.nc')
        v_index = v_da.sel(longitude=slice(lon-1,lon+1),latitude=slice(lat+1,lat-1))
        v_index = v_index.mean(dim=('longitude','latitude'))
        v_df[index] = v_index
    v_df.to_csv('/Users/zeqinhuang/Documents/paper/acid_rain/ERA5_data/' + v + '_for_acid_rain_stations.csv')

'''Created on 13/10/2024
    @author: lkrakow'''
'''Importing libraries'''

import numpy as np
import pandas as pd
import matplotlib as plt

'''Sorting of first data file'''
'''Importing csv file"'''
file_name = r"C:\Users\Windows\Downloads\sea-level.csv"

'''Reading csv file, removing first three rows'''
sealevel = pd.read_csv(file_name)
print(sealevel)

'''Sorting data

Removing unnecessary columns
data.drop(['Name of column'], axis=1)

Renaming columns
df = pd.Dataframe(data)
df.rename(columns={'Old name':'New name'})'''

sealevel = sealevel.drop(['Entity','Code','Global sea level according to Church and White (2011)','Global sea level according to UHSLC'], axis=1)
sealevel = pd.DataFrame(sealevel)
sealevel.rename(columns={'Global sea level as an average of Church and White (2011) and UHSLC data': 'Sea level'}, inplace=True)
sealevel.rename(columns={'Day': 'Time'}, inplace=True)
print(sealevel)

'''Checking the data type'''
sealevel.info()

'''Converting values for Time to datetime'''
sealevel['Time'] = pd.to_datetime(sealevel['Time'], errors='coerce')
sealevel.info()

'''Averaging sea level per year'''
print("NaT values in 'Time' column:", sealevel['Time'].isna().sum())
sealevel['year'] = sealevel['Time'].dt.year
print(sealevel)
average_sealevel_per_year = sealevel.groupby('year')['Sea level'].mean().reset_index()
average_sealevel_per_year.columns = ['year', 'average_sea_level']
print(average_sealevel_per_year)
sealevel = average_sealevel_per_year

'''Setting Year as index'''
sealevel = sealevel.set_index('year')
print(sealevel)
'''Our data for sea level is sorted per average per year'''



'''Sorting of second data file'''
'''Importing csv file"'''
file_name1 = r"C:\Users\Windows\Downloads\global-monthly-temp-anomaly.csv"

'''Reading csv file, removing first three rows'''
tempanomaly = pd.read_csv(file_name1)
print(tempanomaly)

'''Sorting data

Removing unnecessary columns
data.drop(['Name of column'], axis=1)

Renaming columns
df = pd.Dataframe(data)
df.rename(columns={'Old name':'New name'})'''

tempanomaly = tempanomaly.drop(['Entity','Code'], axis=1)
tempanomaly = pd.DataFrame(tempanomaly)
tempanomaly.rename(columns={'Global warming: monthly temperature anomaly': 'Temperature anomaly'}, inplace=True)
tempanomaly.rename(columns={'Day': 'Time'}, inplace=True)
print(tempanomaly)

'''Checking the data type'''
tempanomaly.info()

'''Converting values for Time to datetime'''
tempanomaly['Time'] = pd.to_datetime(tempanomaly['Time'], errors='coerce')
tempanomaly.info()

'''Averaging sea level per year'''
print("NaT values in 'Time' column:", tempanomaly['Time'].isna().sum())
tempanomaly['year'] = tempanomaly['Time'].dt.year
print(tempanomaly)
average_tempanomaly_per_year = tempanomaly.groupby('year')['Temperature anomaly'].mean().reset_index()
average_tempanomaly_per_year.columns = ['year', 'average_tempanomaly_per_year']
print(average_tempanomaly_per_year)
tempanomaly = average_tempanomaly_per_year

'''Setting Year as index'''
tempanomaly = tempanomaly.drop(df.index[141:145])
tempanomaly = tempanomaly.set_index('year')
print(tempanomaly)

'''Both our data are sorted per year and have the same shape'''

Final = pd.merge(sealevel, tempanomaly, on='year')
print(Final)

Final.plot.scatter(x="average_tempanomaly_per_year", y="average_sea_level")
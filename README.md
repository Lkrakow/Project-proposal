# Sea-level & temeprature anomaly plotting
Signal &amp; Systems practical #1
Laurence Krakow s5944600

* Project Overview

Sea-level & temeprature anomaly plotting is a python project which reads two csv file: one with the yearly average of sea levels and one with the yearly averaged temeprature anomaly. This script sorts the data out in order to obtain two datasets of the same format. Once the two datasets have identical shape they are merged into one single dataset and saved as a new file. After following all of those steps, we can plot sea level versus temperature anomaly and see what is the relationship between both variables. 

* Libraries

This project uses two libraries

Numpy: this library is used to conduct numerical operations

Pandas: this library is used for data manipulation and analysis 

* Dataset 1

The first csv file is retrived from Our World in Data and shows Sea level rise. The csv file gives the "Global mean sea level rise is measured relative to the 1993 - 2008 average sea level" (NOAA Climate.gov (2022) – processed by Our World in Data) dating from 1880 to 2020. 

Full source dataset 1: NOAA Climate.gov (2022) – processed by Our World in Data. “Average of Church and White (2011) and UHSLC” [dataset]. NOAA Climate.gov, “Climate Change: Global Sea Level” [original data].

* Dataset 2

The second csv file is retrived from Our World In Data and shows monthly global temeprature anomaly.The csv file gives the "Combined land-surface air and sea-surface water temperature anomaly, given as the deviation from the 1951-1980 mean, in degrees Celsius." (NASA Goddard Institute for Space Studies (2024) - processed by Our World in Data)

Full source dataset 2: NASA Goddard Institute for Space Studies - GISS Surface Temperature Analysis (2024) – with minor processing by Our World in Data

* Methodology 

The first step is to import and read the data

Example:

    File_name = r"file_path"
    Data = pd.read_csv(file_name)

The second step is to remove the columns that we will not use and rename the ones we are interested in

Example:
    Data = Data.drop(['Column to be deleted'], axis=1)
    Data = pd.DataFrame(Data)
    Data.rename(columns={'Old name': 'New name'}, inplace=True)
   

The third step is to set the Time data type as datetime

Example: 
    
    Data['Column of Time'] = pd.to_datetime(Data['Column of Time'], errors='coerce')

The fourth step is format the data to a yearly average so both datasets have the same shape

Example:
   
    print("NaT values in 'Column of Time' column:", Data['TColumn of Time'].isna().sum())
    Data['year'] = Data['Column of Time'].dt.year
    average_data_per_year = Data.groupby('year')['Data'].mean().reset_index()
    average_data_per_year.columns = ['year', 'average_data']
    Data = average_Data_per_year

The fifth step is to set the Year as the index of our data

Example: 
    
    Data = Data.set_index('year')

Once this is done for both dataset and we have the same shape, we can merge both datasets, plot them and save the new dataset

Example:
    
    Datasetnew = pd.merge(Data1, Data2, on='year')
    Datasetnew.plot.scatter(x="variable for temperature anomaly", y="avariable for sea level")
    Datasetnew.to_csv

* What can this project be used for?

This script can be used to format two dataset and merge them in order to plot them. 
# Sea-level & temeprature anomaly plotting
Signal &amp; Systems practical #1
Laurence Krakow s5944600

* Project Overview

Sea-level & temeprature anomaly plotting is a python project which reads two csv file: one with the yearly average of sea levels and one with the yearly averaged temeprature anomaly. This script cleans two datasets and merges them in order to be able to plot the sea level rise versus the temperature anomaly. This allows us to observe the potential relationship between the two variables. 

* Libraries

This project uses two libraries

Numpy: this library is used to conduct numerical operations

Pandas: this library is used for data manipulation and analysis 

* Dataset 1

The first csv file is retrived from Our World in Data and shows Sea level rise. The csv file gives the "Global mean sea level rise is measured relative to the 1993 - 2008 average sea level" (NOAA Climate.gov (2022) – processed by Our World in Data) dating from 1880 to 2020. 

Full source dataset 1: NOAA Climate.gov (2022) – processed by Our World in Data. “Average of Church and White (2011) and UHSLC” [dataset]. NOAA Climate.gov, “Climate Change: Global Sea Level” [original data].
Link: https://ourworldindata.org/grapher/sea-level 

* Dataset 2

The second csv file is retrived from Our World In Data and shows monthly global temeprature anomaly.The csv file gives the "Combined land-surface air and sea-surface water temperature anomaly, given as the deviation from the 1951-1980 mean, in degrees Celsius." (NASA Goddard Institute for Space Studies (2024) - processed by Our World in Data)

Full source dataset 2: NASA Goddard Institute for Space Studies - GISS Surface Temperature Analysis (2024) – with minor processing by Our World in Data
Link: https://ourworldindata.org/grapher/global-monthly-temp-anomaly 

* How to use

The first step is to import and read the datasets using the function "importing_csv_file"

    The user is expected to enter a valid file_path in the terminal in order to access the csv file

    Location first file
    Location second file


The second step is to drop the columns that will not be used

    The user has to provide the index of the columns he/she wishes to drop

    ['Entity', 'Code', 'Day', 'Global sea level according to Church and White (2011)', 'Global sea level according to UHSLC', 'Global sea level as an average of Church and White (2011) and UHSLC data']
    Give us the index of the columns to remove. (e.g. input "23" to keep column remove 2 and 3)
    ['Day', 'Global sea level as an average of Church and White (2011) and UHSLC data']
    ['Entity', 'Code', 'Day', 'Global warming: monthly temperature anomaly']
    Give us the index of the columns to remove. (e.g. input "23" to keep column remove 2 and 3)
    ['Day', 'Global warming: monthly temperature anomaly']


The third step is to set the Time data type as datetime

    In this step, the user is expected to provide the index of the columns they wish to drop


 

* What can this project be used for?

This script can be used to format two dataset and merge them in order to plot them. This can later be used for statistical analysis of the relationship between two variables. 
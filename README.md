# Sea-level & temeprature anomaly plotting
Signal &amp; Systems practical #1
Laurence Krakow s5944600

* Project Overview

Sea-level & temeprature anomaly plotting is a python project which reads two csv file: one with the yearly average of sea levels and one with the yearly averaged temeprature anomaly. This script cleans two datasets and merges them in order to be able to plot the sea level rise versus the temperature anomaly. This allows us to observe the potential relationship between the two variables. 

* Libraries

This project uses one library

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

The first part of the project deals with the import of the csv files needed:

The first step is to import the csv file using the function get_names

    The user is expected to enter a valid file_path in the terminal in order to access the csv file

    Example:

    Give first location
    Give second location

    If the user omits to put in a csv file, a default csv will be used using the config function

The second step is to read the csv file using the importing_csv_file function

At this point: both dataset should be imported and read which leads to the second part of this project: the data cleaning:

The first step is to drop the columns which will not be necessary using the function drop_columns. In the case of this project, we wish to ony look at columns containing a date and the data we are looking at: sea-level or temperature anomaly. This functions requires for the user to give the index of the columns they wish to drop and will rename the columns for both datasets as being 'time' and 'data(1or 2)'. If the user does not input an index, columns of a certain integers will automatically be dropped leaving only the time and data columns.

    Example:

    ['Entity', 'Code', 'Day', 'Global sea level according to Church and White (2011)', 'Global sea level according to UHSLC', 'Global sea level as an average of Church and White (2011) and UHSLC data']
    Give us the index of the columns to remove. (e.g. input "23" to remove column 2 and 3)
    ['Day', 'Global sea level as an average of Church and White (2011) and UHSLC data']
    ['Entity', 'Code', 'Day', 'Global warming: monthly temperature anomaly']
    Give us the index of the columns to remove. (e.g. input "23" to remove column 2 and 3)
    ['Day', 'Global warming: monthly temperature anomaly']

The second step is to to convert the time variable into a datetime type in order to manipulate it later on in the project. 

Here the cleaning of the data is done and now it has to be merged into a single dataset:

The first step is to extract each datset's limit in terms of year because we can only merge two datsets of the same size using the function get_date_limits 

The second step is to create a merge dataset table which will have the right year limits in order for both data to be available. This is done using the function initialise_merged_data_set. This creates a table with year and two empty columns data1 and data2

The third and last step is to use the function fill_merged_set to fill in the table with the data from the csv files. In order to do so we need to average the values per year because in the sealevel dataset we have data for four month a year and in the temperature anomaly dataset we have data for each twelve month. Therefore, for the format of both dataset to be identical so it can be compared we average the values per year then fill them in the table. 

* What can this project be used for?

This script can be used to format two dataset and merge them in order to plot them. This can later be used for statistical analysis of the relationship between two variables. 
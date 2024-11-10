"""Last updated 10/11/2024 @author: lkrakow"""
import pandas as pd

def get_date_limits(file1: pd.DataFrame, file2: pd.DataFrame) -> list:
    """See what are the year limits of both dataset
    
    Args:
    Dataset 1 & 2
    
    Return:
    Year min and max limit of both dataset"""
    
    first_year_file1 = file1['time'].iloc[0].year
    first_year_file2 = file2['time'].iloc[0].year
    last_year_file1 = file1['time'].iloc[-1].year
    last_year_file2 = file2['time'].iloc[-1].year
    
    return [first_year_file1, first_year_file2, last_year_file1, last_year_file2]

def initialise_merged_data_set(limits: list) -> pd.DataFrame:
    """Initialize a DataFrame to store merged data for the correct range of years.
    the correct range is the intersection of file1's years and file2's years.
    
    Args:
    list of the limits of the datasets
    
    Return:
    A DataFrame with a "Year" column for each year in the range and placeholder columns "Data1" and "Data2" filled with zeroes."""
    
    if (limits[0] < limits[1]):
        start = limits[1]
    else:
        start = limits[0]
    if (limits[2] < limits[3]):
        end = limits[2]
    else:
        end = limits[3]
    
    if pd.isna(start) or pd.isna(end):
        print("Error: One or both limit values are NaN.")
        return None
    
    number_of_year = int(end - start + 1)
    merged_data_set = pd.DataFrame(0, index=range(number_of_year), columns=["Year", "Data1", "Data2"])
    merged_data_set['Year'] = range(start, end + 1)
    
    return merged_data_set

def fill_merged_set(merged_data_set: pd.DataFrame, file1: pd.DataFrame, file2: pd.DataFrame, limits: list) -> pd.DataFrame:
    """Fill a merged dataset with yearly average values from two data files over the range of years.
    
    Args:
    two datasets  containing time-series data with columns "time" and "data
    
    Return:
    The merged_data_set DataFrame filled with yearly average values for "Data1" and "Data2"""
    
    file1['year'] = file1['time'].dt.year
    yearly_average_data1 = file1.groupby('year')['data'].mean().reset_index()
    file2['year'] = file2['time'].dt.year
    yearly_average_data2 = file2.groupby('year')['data'].mean().reset_index()

    start_year = max(limits[0], limits[1])
    end_year = min(limits[2], limits[3])
    yearly_average_data1 = yearly_average_data1[(yearly_average_data1['year'] >= start_year) & (yearly_average_data1['year'] <= end_year)]
    yearly_average_data2 = yearly_average_data2[(yearly_average_data2['year'] >= start_year) & (yearly_average_data2['year'] <= end_year)]
    
    merged_data_set['Data1'] = yearly_average_data1['data']
    merged_data_set['Data2'] = yearly_average_data2['data']
    
    return merged_data_set




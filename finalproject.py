'''Updated on 10/11/2024 @author: lkrakow'''

import pandas as pd

def get_names(config: dict) -> list:
    file_name1 = input("Give first location ")
    if (file_name1 == ""):
        file_name1 = config['init_csv']['file_name1_default_location']
    
    file_name2 = input("Give second location ")
    if (file_name2 == ""):
        file_name2 = config['init_csv']['file_name2_default_location']
        
    return [file_name1, file_name2]

def importing_csv_file (file1_path, file2_path):
    """Imports csv files
    
    Args:
    File1: path to the first csv file
    File2: path to the second csv file
    
    Return:
    prints the two csv file as tables"""
    
    #if file1_path == "":
    #       file1_path = r"C:\Users\Windows\pythonproject\Project-proposal\sea-level.csv"
    try: 
        data1 = pd.read_csv(file1_path)
        print("Data 1:")
        print(data1)
    except FileNotFoundError:
        print(f"Error: {file1_path} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: {file1_path} is empty.")
    except pd.errors.ParserError:
        print(f"Error: {file1_path} contains malformed CSV data.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

    #if file2_path == "":
    #        file2_path = r"C:\Users\Windows\pythonproject\Project-proposal\global-monthly-temp-anomaly.csv"
    try:
        data2 = pd.read_csv(file2_path)
        print("Data 2:")
        print(data2)
    except FileNotFoundError:
        print(f"Error: {file2_path} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: {file2_path} is empty.")
    except pd.errors.ParserError:
        print(f"Error: {file2_path} contains malformed CSV data.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        
    return [data1, data2]

def drop_columns(file: pd.DataFrame, config: dict, config_key: str) -> pd.DataFrame:
    """Cleans the data by dropping unnecessary columns
    
    Args:
    data1 = first dataset to clean
    data2 = second dataset to clean
    
    Return:
    Cleaned dataframes"""
    
    headers_file = list(file.columns)
    print(headers_file)
    to_keep: str = input("Give us the index of the columns to remove. (e.g. input \"23\" to keep column remove 2 and 3)")
    if (to_keep == ""):
        to_keep = config["init_csv"][config_key]
    how_many: int = len(to_keep)
    while (how_many > 0):
        file = file.drop([headers_file[int(to_keep[how_many - 1])]], axis=1)
        how_many -= 1
    columns_names = list(file.columns)
    print(columns_names)
    file = file.rename(columns={columns_names[0]:"time"})
    file = file.rename(columns={columns_names[1]:"data"})
    return file

def get_headers(data1: pd.DataFrame, data2: pd.DataFrame, config: dict) -> list:
    data1 = drop_columns(data1, config, "column_drop_default_index1")
    data2 = drop_columns(data2, config, "column_drop_default_index2")
    return [data1, data2]

def convert_to_datetime(file1: pd.DataFrame, file2: pd.DataFrame) -> list:
    """Convert a selected column to datetime
    
    Args:
    Data column with time
    
    Return:
    Data column with datatype = datetime"""

    print(list(file1.columns))
    file1['time'] = pd.to_datetime(file1['time'], errors='coerce')
    print(list(file2.columns))
    file2['time'] = pd.to_datetime(file2['time'], errors='coerce')
    
    return [file1, file2]

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

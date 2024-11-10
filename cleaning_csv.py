"""Last update 10/11/2024 @author: lkrakow"""
import pandas as pd

def drop_columns(file: pd.DataFrame, config: dict, config_key: str) -> pd.DataFrame:
    """Cleans the data by dropping unnecessary columns
    
    Args:
    data1 = first dataset to clean
    data2 = second dataset to clean
    
    Return:
    Cleaned dataframes"""
    
    headers_file = list(file.columns)
    print(headers_file)
    to_keep: str = input("Give us the index of the columns to remove. (e.g. input \"23\" to remove column 2 and 3)")
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


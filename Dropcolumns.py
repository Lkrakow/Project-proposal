import pandas as pd

def drop_columns(file: pd.DataFrame) -> None:
    """Cleans the data by dropping unnecessary columns
    
    Args:
    data1 = first dataset to clean
    data2 = second dataset to clean
    
    Return:
    Cleaned dataframes"""
    
    headers_file = list(file.columns)
    print(headers_file)
    to_keep: str = input("Give us the index of the columns to remove. (e.g. input \"23\" to keep column remove 2 and 3)")
    how_many: int = len(to_keep)
    while (how_many > 0):
        file = file.drop([headers_file[int(to_keep[how_many - 1])]], axis=1)
        how_many -= 1
    print(list(file.columns))
    return



def get_headers(data1: pd.DataFrame, data2: pd.DataFrame) -> None:
    data1 = drop_columns(data1)
    data2 = drop_columns(data2)
    return


import pandas as pd

def convert_to_datetime(file1: pd.DataFrame, file2: pd.DataFrame, default_select1: str, default_select2: str) -> pd.DataFrame:
    """Convert a selected column to datetime
    
    Args:
    Data column with time
    
    Return:
    Data column with datatype = datetime"""
    select1 = input("What is the name of the column containing time ? ")
    print(list(file1.columns))
    if (select1 == ""):
        select1 = default_select1
    file1[select1] = pd.to_datetime(file1[select1], errors='coerce')
    
    select2 = input("What is the name of the column containing time ? ")
    print(list(file2.columns))
    if (select2 == ""):
        select2 = default_select1
    file2[select2] = pd.to_datetime(file1[select2], errors='coerce')
    
    print(file1)
    return [file1, file2]



'''Last update 10/11/2024 @author: lkrakow'''

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

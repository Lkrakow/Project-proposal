'''Created on 10/11/2024 @author: lkrakow'''
'''Importing libraries'''

import numpy as np
import pandas as pd
import matplotlib as pd

def importing_csv_file (file1_path, file2_path):
    """Imports csv files
    
    Args:
    File1: path to the first csv file
    File2: path to the second csv file
    
    Return:
    prints the two csv file as tables"""
    
    try: 
        if file1_path == "":
            file1_path = "C:\Users\Windows\pythonproject\Project-proposal\sea-level.csv"
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

        
    try:
        if file2_path == "":
            file2_path = "C:\Users\Windows\pythonproject\Project-proposal\global-monthly-temp-anomaly.csv"
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
    
test = importing_csv_file(input(""), input(""))
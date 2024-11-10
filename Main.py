import numpy as np
import pandas as pd
import ImportingCSV
import Dropcolumns

input1 = input("Location first file")
input2 = input("Location second file")
test = importing_csv_file(input1, input2)
Dropcolumns.get_headers(test[0], test[1])
"""Last updated 10/11/2024 @author:lkrakow"""
import toml

import importing_csv
import cleaning_csv
import merging_data

with open('config.toml', 'r') as f:
    configs = toml.load(f)

print(type(configs))

file_names: list = importing_csv.get_names(configs)
data_collection: list = importing_csv.importing_csv_file(file_names[0], file_names[1])

data_collection = cleaning_csv.get_headers(data_collection[0], data_collection[1], configs)
data_collection = cleaning_csv.convert_to_datetime(data_collection[0], data_collection[1])

merged_data_limits = merging_data.get_date_limits(data_collection[0], data_collection[1])
merged_data = merging_data.initialise_merged_data_set(merged_data_limits)
merged_data = merging_data.fill_merged_set(merged_data, data_collection[0], data_collection[1], merged_data_limits)
print(merged_data)

merged_data.plot(kind='scatter', x='Data1', y='Data2', color='red', marker='o')
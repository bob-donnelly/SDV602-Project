"""
This module converts the excel file into the timber.json file for the purposes of local data services and is not involved 
in the marking requirements.
"""

# Importing necessary libraries

import pandas

# Using pandas to read excel as a dataframe

excel_data_df = pandas.read_excel('excel.xlsx', sheet_name = 'Raw Data')

# Exporting data that is converted from excel into json orientated by index and indented in a json style.

json_str = excel_data_df.to_json('timber.json', orient='index', indent=2)

# Printed in console to check before exporting to a file.

# print('Excel to JSON:\n', json_str)
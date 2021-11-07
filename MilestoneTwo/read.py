"""
Reading the local data from the local json file.
The base data parsing function.
"""
import pandas as pd

def returnValues():
    pd.set_option('display.max_rows', None)
    timber = pd.read_json('timber.json', orient='index')

    return timber
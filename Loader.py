import pandas as pd
"""
Receives the path to the data (csv format) and returns a pandas dataframe
"""

def load(path):
    try:
        return pd.read_csv(path)
    except:
        print('There was a problem loading the data')


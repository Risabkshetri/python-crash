# src/data_loader.py

import pandas as pd

def load_data(filepath):
    """
    Load subscriber data from a CSV file.
    """
    data = pd.read_csv(filepath, parse_dates=['date'])
    return data

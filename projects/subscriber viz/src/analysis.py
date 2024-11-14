# src/analysis.py

import pandas as pd

def calculate_growth(data):
    """
    Calculate daily growth in subscribers for each YouTuber.
    """
    data['growth'] = data.groupby('youtuber')['subscribers'].diff().fillna(0)
    return data

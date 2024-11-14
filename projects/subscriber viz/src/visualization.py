# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_subscriber_count(data):
    """
    Plot the subscriber count over time for each YouTuber.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='date', y='subscribers', hue='youtuber', marker='o')
    plt.title('YouTuber Subscriber Count Over Time')
    plt.xlabel('Date')
    plt.ylabel('Subscribers')
    plt.legend(title='YouTuber')
    plt.show()

def plot_growth(data):
    """
    Plot the growth in subscribers for each YouTuber.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='date', y='growth', hue='youtuber', marker='o')
    plt.title('Daily Subscriber Growth')
    plt.xlabel('Date')
    plt.ylabel('Subscriber Growth')
    plt.legend(title='YouTuber')
    plt.show()

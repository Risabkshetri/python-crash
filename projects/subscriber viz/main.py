# main.py

from src.data_loader import load_data
from src.analysis import calculate_growth
from src.visualization import plot_subscriber_count, plot_growth

def main():
    # Load data
    filepath = 'data/mock_data.csv'
    data = load_data(filepath)
    
    # Analyze data
    data = calculate_growth(data)
    
    # Visualize data
    plot_subscriber_count(data)
    plot_growth(data)

if __name__ == "__main__":
    main()

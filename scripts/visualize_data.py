import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the sentiment analysis CSV file
def load_data(filename):
    return pd.read_csv(filename)

# Plot sentiment distribution
def plot_sentiment_distribution(df, output_path):
    sentiment_counts = df['sentiment'].value_counts()
    
    plt.figure(figsize=(8, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.savefig(os.path.join(output_path, 'sentiment_distribution.png'))
    plt.show()

# Plot sentiment over time
def plot_sentiment_over_time(df, output_path):
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['date'] = df['created_at'].dt.date

    sentiment_by_date = df.groupby(['date', 'sentiment']).size().unstack(fill_value=0)

    plt.figure(figsize=(12, 8))
    sentiment_by_date.plot(kind='line', marker='o')
    plt.title('Sentiment Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Tweets')
    plt.legend(title='Sentiment')
    plt.savefig(os.path.join(output_path, 'sentiment_trends_over_time.png'))
    plt.show()

# Main function
def main():
    input_file = input("Enter the path of the sentiment analysis CSV file: ")
    output_folder = "visualizations"
    
    os.makedirs(output_folder, exist_ok=True)
    
    print("Loading data...")
    df = load_data(input_file)
    
    print("Generating sentiment distribution plot...")
    plot_sentiment_distribution(df, output_folder)
    
    print("Generating sentiment trends over time plot...")
    plot_sentiment_over_time(df, output_folder)

    print(f"Visualizations saved in the '{output_folder}' folder.")

if __name__ == "__main__":
    main()
import pandas as pd
from textblob import TextBlob
import os

# Load the CSV file
def load_tweets(filename):
    return pd.read_csv(filename)

# Perform sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Add sentiment analysis to the DataFrame
def add_sentiment(df):
    df["sentiment"] = df["text"].apply(analyze_sentiment)
    return df

# Save the DataFrame with sentiment analysis to a new CSV file
def save_to_csv(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Saved sentiment analysis results to {filename}")

# Main function
def main():
    input_file = input("Enter the path of the CSV file with tweets: ")
    output_file = input("Enter the path to save the sentiment analysis CSV: ")

    print("Loading tweets...")
    df = load_tweets(input_file)

    print("Analyzing sentiment...")
    df = add_sentiment(df)

    save_to_csv(df, output_file)

if __name__ == "__main__":
    main()
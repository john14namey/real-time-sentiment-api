from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

# Load the sentiment analysis CSV file
DATA_FILE = "data/tweets_nfl_sentiment.csv"

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return None

@app.route('/')
def home():
    return "Welcome to the Real-Time Sentiment Analysis API!"

# Endpoint to get all tweets
@app.route('/tweets', methods=['GET'])
def get_tweets():
    df = load_data()
    if df is not None:
        return jsonify(df.to_dict(orient='records'))
    else:
        return jsonify({"error": "Data file not found"}), 404

# Endpoint to get tweets by sentiment
@app.route('/tweets/sentiment/<sentiment>', methods=['GET'])
def get_tweets_by_sentiment(sentiment):
    df = load_data()
    if df is not None:
        filtered_df = df[df['sentiment'].str.lower() == sentiment.lower()]
        return jsonify(filtered_df.to_dict(orient='records'))
    else:
        return jsonify({"error": "Data file not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get Heroku's assigned PORT or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)  # Bind to 0.0.0.0 for external access
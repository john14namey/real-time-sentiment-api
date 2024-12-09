import tweepy
import pandas as pd
import os
from datetime import datetime



import tweepy
import pandas as pd
import os
from datetime import datetime

# Twitter API credentials (replace with your actual credentials)
API_KEY = "wrsaH34PC3PbpP78fK7F9jDrH"
API_SECRET = "dcSjztgOSwlGDrLAsM8VzTJtHDseZ9tRPUsUsXyLxyZYfS2P5x"
ACCESS_TOKEN = "1528047445325885441-6u3FbbsnDWBEkfuAvb8kGVLnxSU1KH"
ACCESS_TOKEN_SECRET = "Y5BpbOWXdLHZjtxrXzp22ZmSvrbNI2Esbkkp7ri3OVVKu"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAETQxQEAAAAANA0MT0pwRnYZWLgC00%2FE1ZCGJIM%3DR7NOskoikGz9Q7jZE2wS774O9Y7NV2wqtlazHMyhpzieaREj11"

# Authenticate with the Twitter API v2
def authenticate_twitter():
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    return client

# Fetch tweets based on a keyword using Twitter API v2
def fetch_tweets(client, keyword, count=100):
    tweets_data = []
    try:
        # Using the v2 API search endpoint
        response = client.search_recent_tweets(query=keyword, tweet_fields=["created_at"], max_results=count)
        for tweet in response.data:
            tweets_data.append({
                "created_at": tweet.created_at,
                "username": tweet.author_id,
                "text": tweet.text
            })
    except tweepy.errors.TweepyException as e:
        print(f"Error: {e}")

    return tweets_data

# Save tweets to a CSV file
def save_to_csv(tweets_data, filename="data/tweets.csv"):
    df = pd.DataFrame(tweets_data)
    # Create the data folder if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # Save the data to CSV
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} tweets to {filename}")

# Main function
def main():
    client = authenticate_twitter()
    keyword = input("Enter keyword to search for tweets: ")
    count = int(input("Enter the number of tweets to fetch (max 100): "))
    print(f"Fetching {count} tweets about '{keyword}'...")
    tweets = fetch_tweets(client, keyword, count)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/tweets_{keyword}_{timestamp}.csv"
    save_to_csv(tweets, filename)

if __name__ == "__main__":
    main()


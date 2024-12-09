import tweepy

# Replace these placeholders with your actual Twitter API credentials
API_KEY = "wrsaH34PC3PbpP78fK7F9jDrH"
API_SECRET = "dcSjztgOSwlGDrLAsM8VzTJtHDseZ9tRPUsUsXyLxyZYfS2P5x"
ACCESS_TOKEN = "1528047445325885441-6u3FbbsnDWBEkfuAvb8kGVLnxSU1KH"
ACCESS_TOKEN_SECRET = "Y5BpbOWXdLHZjtxrXzp22ZmSvrbNI2Esbkkp7ri3OVVKu"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful!")
except Exception as e:
    print(f"Error: {e}")

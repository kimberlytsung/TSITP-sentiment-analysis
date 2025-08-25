import requests
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import time

BEARER_TOKEN = "" #Replace with your own bearer token
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

#Excludes retweets and non-English tweets
query = "The Summer I Turned Pretty -is:retweet lang:en"

#API endpoint
url = "https://api.twitter.com/2/tweets/search/recent"

params = {
    "query": query,
    "max_results": 50,
    "tweet.fields": "created_at,text"
}

r = requests.get(url, headers=headers, params=params)

if r.status_code != 200:
    raise Exception(f"Error fetching tweets: {r.status_code} {r.text}")

data = r.json()["data"]

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    polarity = (analysis.sentiment).polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else: 
        return "Neutral"

tweets = []
timestamps = []
sentiments = []

for tweet in data:
    text = tweet["text"]
    sentiment = analyze_sentiment(text)
    tweets.append(text)
    sentiments.append(sentiment)
    timestamps.append(tweet["created_at"])
    time.sleep(2)

df = pd.DataFrame({
    "Tweet": tweets,
    "Sentiment": sentiments,
    "Timestamp": timestamps
})

#Plotting sentiment distribution on a bar chart
df["Sentiment"].value_counts().plot(kind="bar", title="Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.show()

df.to_csv("TSITP_sentiment_analysis.csv", index=False)
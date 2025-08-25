import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from io import BytesIO

df = pd.read_csv("TSITP_sentiment_analysis.csv")

st.title("Sentiment Analysis Dashboard: The Summer I Turned Pretty")

#decide after on whether this worth keeping
if st.checkbox("Show raw data"):
    st.dataframe(df)

#Filter by sentiment
sentiment_options = st.multiselect(
    "Select sentiment(s):",
    options=["Positive", "Neutral", "Negative"]
)

filtered_df = df[df["Sentiment"].isin(sentiment_options)]
st.write(f"Showing {len(filtered_df)} tweets")

#Sentiment distribution plot
figure, axis = plt.subplots()

if not filtered_df.empty and "Sentiment" in filtered_df.columns:
    filtered_df["Sentiment"].value_counts().plot(kind="bar", ax=axis)
else:
    print("No data to plot.")
axis.set_xlabel("Sentiment")
axis.set_ylabel("Number of Tweets")
axis.set_title("Sentiment Distribution")
st.pyplot(figure)

#Search tweets by keyword
keyword = st.text_input("Search tweets by keyword:")
if keyword:
    keyword_filtered = filtered_df[filtered_df["Tweet"].str.contains(keyword, case=False, na=False)]
    st.write(f"### Tweets containing '{keyword}':")
    st.dataframe(keyword_filtered, hide_index=True)

# Color functions (Green = Positive, Red = Negative, Yellow = Neutral)
def green_color_func(*args, **kwargs):
    return "rgb(0, 150, 0)"

def red_color_func(*args, **kwargs):
    return "rgb(200, 0, 0)"

def yellow_color_func(*args, **kwargs):
    return "rgb(200, 200, 0)"

def generate_wordcloud(text, sentiment):
    stopwords = set(STOPWORDS)
    color_function = {
        "Positive": green_color_func,
        "Negative": red_color_func,
        "Neutral": yellow_color_func
    }

    wordcloud = WordCloud(
        background_color="white",
        stopwords=stopwords,
        width=1600,
        height=800,
        max_words=100,
        max_font_size=50,
        random_state=42,
        color_func=color_function.get(sentiment, None)
    ).generate(text)
    return wordcloud

st.write("## Word Clouds by Sentiment")

#Select Sentiment for display
wc_sentiment = st.selectbox(
    "Select sentiment to view word cloud:",
    options=["Positive", "Negative", "Neutral"]
)

wc_text = " ".join(filtered_df[filtered_df["Sentiment"] == wc_sentiment]["Tweet"].dropna())

if wc_text.strip():
    wordcloud = generate_wordcloud(wc_text, wc_sentiment)
    figure_wc, axis_wc = plt.subplots(figsize=(12, 6))
    axis_wc.imshow(wordcloud, interpolation="bilinear")
    axis_wc.axis("off")
    st.pyplot(figure_wc)
else:
    st.write("No tweets available for this sentiment.")

#Option to download filtered data as CSV
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(label="Download filtered data as CSV", data=csv, file_name="filtered_tweets.csv")

#Option to download wordcloud as image
buf = BytesIO()
figure_wc.savefig(buf, format="png", dpi=300)
buf.seek(0)
st.download_button(
    label="Download Word Cloud as PNG",
    data=buf,
    file_name="Sentiment_wordcloud.png",
    mime="image/png"
)
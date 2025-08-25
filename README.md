## TSITP-sentiment-analysis

**Objective**

This project aims to analyze real-time public sentiment about the most recent season of the TV show “The Summer I Turned Pretty” (TSITP) using Twitter/X data. It retrieves tweets using the Twitter API, performs sentiment analysis with TextBlob, and visualizes the data in an interactive Streamlit dashboard.

**Features**

* Collects recent tweets mentioning _The Summer I Turned Pretty_.
* Filters out retweets and non-English tweets
* Creates sentiment analysis bar chart distribution
* Exports results to `TSITP_sentiment_analysis.csv`
* Interactive Streamlit app with:
  * Raw data viewer
  * Sentiment filter
  * Sentiment distribution bar chart
  * Word cloud of frequent terms

**Results**

![TSITP Sentiment Analysis Bar Chart](https://github.com/kimberlytsung/TSITP-sentiment-analysis/blob/main/Images/TSITP_sentiment_distribution.png)

Sentiment distribution showed a majority of positive tweets, implying approving audience reception. 

**Dashboard Display**

Keyword Search 
![Sentiment Analysis Keyword Search](https://github.com/kimberlytsung/TSITP-sentiment-analysis/blob/main/Images/TSITP_app_keyword_search.png)

Word Cloud
![Positive Sentiment Word Cloud](https://github.com/kimberlytsung/TSITP-sentiment-analysis/blob/main/Images/TSITP_app_wordcloud.png)

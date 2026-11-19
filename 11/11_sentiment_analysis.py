# 11. Case study: sentiment analysis of tweets about vaccination.
#     Dataset: vaccination_tweets.csv (put it in this folder).
#     Only the "text" column (the tweet) is used.

import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the NLTK data this program needs (skipped if already downloaded)
nltk.download("punkt", quiet=True)          # tokenizer (old NLTK)
nltk.download("punkt_tab", quiet=True)      # tokenizer (new NLTK)
nltk.download("stopwords", quiet=True)      # stop word list
nltk.download("vader_lexicon", quiet=True)  # sentiment scores

# Step 1: load the dataset
import pandas as pd

df = pd.read_csv("vaccination_tweets.csv")

# print("Columns:", list(df.columns))
# print("Number of tweets:", len(df))

df = df[["text"]].dropna()

# Step 2: remove links (almost every tweet has one, and "https" would
#         otherwise be the most common word in Step 6)
df["text"] = df["text"].str.replace(r"http\S+", "", regex=True)

# Step 3: score each tweet with VADER and label it (same labels as program 6a).
# Stop words are NOT removed here, because words like "not" change the sentiment.
sia = SentimentIntensityAnalyzer()

def get_score(tweet):
    return sia.polarity_scores(tweet)["compound"]

def get_label(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df["score"] = df["text"].apply(get_score)
df["sentiment"] = df["score"].apply(get_label)

print("\nFirst 5 tweets with their sentiment:")
print(df[["text", "score", "sentiment"]].head())

# Step 4: how many tweets are positive, negative and neutral
counts = df["sentiment"].value_counts()
print("\nSentiment counts:")
print(counts)

# Step 5: bar chart of the sentiment counts (close the window to continue)
import matplotlib.pyplot as plt

counts.plot(kind="bar", title="Sentiment of vaccination tweets")
plt.xlabel("Sentiment")
plt.ylabel("Number of tweets")
plt.show()

# Step 6: most common words in all tweets (same steps as program 6b)
stop_words = set(stopwords.words("english"))
text = " ".join(df["text"])          # all tweets joined into one big text
tokens = word_tokenize(text.lower())
words = [w for w in tokens if w.isalpha() and w not in stop_words]

freq = FreqDist(words)
print("\nTop 10 words in the tweets:")
for word, count in freq.most_common(10):
    print(f"{word:<15}{count}")

freq.plot(10, title="Top 10 words in vaccination tweets")
plt.show()

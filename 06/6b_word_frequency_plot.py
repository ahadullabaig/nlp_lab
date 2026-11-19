# 6b. Plot a graph of the most frequent words in a text,
#     without stop words and punctuation.

import matplotlib.pyplot as plt
import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download the NLTK data this program needs (skipped if already downloaded)
nltk.download("punkt", quiet=True)        # tokenizer (old NLTK)
nltk.download("punkt_tab", quiet=True)    # tokenizer (new NLTK)
nltk.download("stopwords", quiet=True)    # stop word list

text = """Artificial intelligence is changing the world. Machine learning is a part of
artificial intelligence, and deep learning is a part of machine learning. Today,
machine learning helps doctors find diseases, helps banks stop fraud and helps
students learn faster. Natural language processing, another part of artificial
intelligence, lets computers read and understand language. As data grows, machine
learning and artificial intelligence will keep changing how we live and work."""

# Step 1: preprocess - lowercase, tokenize, drop stop words and punctuation
stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [w for w in tokens if w.isalpha() and w not in stop_words]

words = preprocess(text)

# Step 2: count how often each word appears
freq = FreqDist(words)

print("Top 10 most frequent words:")
for word, count in freq.most_common(10):
    print(f"{word:<15}{count}")

# Step 3: plot the top 10 words, then show the graph window (close it to finish)
freq.plot(10, title="Top 10 most frequent words")
plt.show()

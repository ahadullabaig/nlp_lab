# 7b. Create a collection of 3 documents, find the frequency of bigrams in the
#     collection, count the bigrams and display the top 5 most common.

import nltk
from nltk import ngrams, FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download the NLTK data this program needs (skipped if already downloaded)
nltk.download("punkt", quiet=True)        # tokenizer (old NLTK)
nltk.download("punkt_tab", quiet=True)    # tokenizer (new NLTK)
nltk.download("stopwords", quiet=True)    # stop word list

documents = [
    "Natural language processing helps computers understand human language. "
    "Machine learning makes natural language processing better.",

    "Machine learning is a part of artificial intelligence. "
    "Deep learning is a type of machine learning.",

    "Artificial intelligence, machine learning and deep learning power "
    "modern natural language processing systems.",
]

# Preprocess - same function as programs 2b and 6b.
# Stop words are removed so pairs like "of the" don't fill the top 5.
# (The question doesn't require this - delete "and w not in stop_words" to keep them.)
stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [w for w in tokens if w.isalpha() and w not in stop_words]

# Make bigrams one document at a time, so no bigram joins the end of
# one document to the start of the next
all_bigrams = []
for doc in documents:
    words = preprocess(doc)
    all_bigrams.extend(ngrams(words, 2))

freq = FreqDist(all_bigrams)

print("Bigram frequencies:")
for bigram, count in freq.items():
    print(bigram, count)

print("\nTotal number of bigrams:", len(all_bigrams))
print("Number of unique bigrams:", len(freq))

print("\nTop 5 most common bigrams:")
for bigram, count in freq.most_common(5):
    print(bigram, count)

# 2b. N-gram model from a given text, excluding stop words.

import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download the NLTK data this program needs (skipped if already downloaded)
nltk.download("punkt", quiet=True)        # tokenizer (old NLTK)
nltk.download("punkt_tab", quiet=True)    # tokenizer (new NLTK)
nltk.download("stopwords", quiet=True)    # stop word list

text = ("I love natural language processing. Natural language processing is fun. "
        "I love learning new languages and I love coding.")

# Step 1: preprocess - lowercase, tokenize, drop stop words and punctuation
stop_words = set(stopwords.words("english"))
tokens = word_tokenize(text.lower())
words = [w for w in tokens if w.isalpha() and w not in stop_words]

print("Words without stop words:", words)

# Step 2: build unigrams, bigrams and trigrams
for n in [1, 2, 3]:
    print(f"\n{n}-grams:", list(ngrams(words, n)))

# # Step 3: bigram model - P(w2 | w1) = count(w1 w2) / count(w1)
# from nltk import FreqDist
# unigram_freq = FreqDist(words)
# bigram_freq = FreqDist(ngrams(words, 2))

# print("\nBigram probabilities:")
# for (w1, w2), count in bigram_freq.items():
#     prob = count / unigram_freq[w1]
#     print(f"P({w2} | {w1}) = {count}/{unigram_freq[w1]} = {prob:.2f}")

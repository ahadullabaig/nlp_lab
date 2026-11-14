# 1b. Preprocessing of text: tokenization, stop word removal and stemming.

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# in case of file usage:
# with open("sample.txt") as file:
#     text = file.read()

text = ("Natural Language Processing is a field of Artificial Intelligence. "
        "It helps computers understand, interpret and generate human languages. "
        "Researchers are building smarter systems every day!")

# Step 1: Tokenization - split the text into sentences, then into words
print("Sentences:", sent_tokenize(text))
tokens = word_tokenize(text.lower())
print("\nTokens:", tokens)

# Step 2: Stop word removal - drop common words (is, a, of, the ...)
#         w.isalpha() also drops punctuation and numbers
stop_words = set(stopwords.words("english"))
words = [w for w in tokens if w.isalpha() and w not in stop_words]
print("\nAfter removing stop words:", words)

# Step 3: Stemming - cut each word down to its root form
stemmer = PorterStemmer()
stems = [stemmer.stem(w) for w in words]
print("\nAfter stemming:", stems)

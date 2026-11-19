# 12. Case study: SMS spam detection.
#     Dataset: spam.csv (put it in this folder).
#     Column v1 is the label (ham/spam) and v2 is the message.

import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Download the NLTK data this program needs (skipped if already downloaded)
nltk.download("punkt", quiet=True)        # tokenizer (old NLTK)
nltk.download("punkt_tab", quiet=True)    # tokenizer (new NLTK)
nltk.download("stopwords", quiet=True)    # stop word list

# Step 1: load the dataset (this file is not UTF-8, so we give the encoding)
df = pd.read_csv("spam.csv", encoding="latin-1")
print("Columns:", list(df.columns))

df = df[["v1", "v2"]]
df.columns = ["label", "message"]
print(df.head())

counts = df["label"].value_counts()
print("\nMessages of each type:")
print(counts)

counts.plot(kind="bar", title="Ham vs Spam messages")
plt.xlabel("Label")
plt.ylabel("Number of messages")
plt.show()

# Step 2: preprocess each message (same function as programs 2b, 6b and 7b)
stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [w for w in tokens if w.isalpha() and w not in stop_words]

def clean_message(message):
    return " ".join(preprocess(message))

df["clean_message"] = df["message"].apply(clean_message)

# Step 3: split into training data (80%) and testing data (20%)
X_train, X_test, y_train, y_test = train_test_split(
    df["clean_message"], df["label"], test_size=0.2, random_state=42)

# Step 4: turn each message into word counts (bag of words)
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)   # learn the vocabulary + count
X_test_counts = vectorizer.transform(X_test)         # only count

# Step 5: train a Naive Bayes classifier and test it
model = MultinomialNB()
model.fit(X_train_counts, y_train)
y_pred = model.predict(X_test_counts)

print("\nAccuracy:", round(accuracy_score(y_test, y_pred), 4))
print("\nConfusion matrix (rows = actual, columns = predicted: ham, spam):")
print(confusion_matrix(y_test, y_pred))
print("\nClassification report:")
print(classification_report(y_test, y_pred))

# Step 6: try the model on new messages
new_messages = [
    "Congratulations! You have won a free iPhone. Call now to claim your prize.",
    "Hey, are we still meeting for lunch tomorrow?",
]
for message in new_messages:
    prediction = model.predict(vectorizer.transform([clean_message(message)]))[0]
    print(f"{prediction:<6}<- {message}")

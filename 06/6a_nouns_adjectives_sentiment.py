# 6a. Identify nouns and adjectives in a sentence using chunking, then
#     calculate the overall sentiment score of the extracted adjectives.

import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the NLTK data this program needs (skipped if already downloaded)
nltk.download("punkt", quiet=True)                           # tokenizer (old NLTK)
nltk.download("punkt_tab", quiet=True)                       # tokenizer (new NLTK)
nltk.download("averaged_perceptron_tagger", quiet=True)      # POS tagger (old NLTK)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)  # POS tagger (new NLTK)
nltk.download("vader_lexicon", quiet=True)                   # sentiment scores

sentence = "The hotel has a beautiful garden and friendly staff, but the rooms are dirty."

# Step 1: tag every word with its part of speech
tagged = nltk.pos_tag(word_tokenize(sentence))
print("POS tags:", tagged)

# Step 2: chunk grammar - one rule for nouns, one for adjectives
grammar = r"""
NOUN: {<NN.*>}
ADJ: {<JJ.*>}
"""
parser = nltk.RegexpParser(grammar)
tree = parser.parse(tagged)

# Step 3: collect the words from each chunk (same loop as program 4b)
nouns = []
adjectives = []
for subtree in tree.subtrees():
    if subtree.label() == "NOUN":
        nouns.append(" ".join(word for word, tag in subtree.leaves()))
    elif subtree.label() == "ADJ":
        adjectives.append(" ".join(word for word, tag in subtree.leaves()))

print("\nNouns:", nouns)
print("Adjectives:", adjectives)

# Step 4: score each adjective with VADER (-1 = very negative, +1 = very positive)
sia = SentimentIntensityAnalyzer()

def get_label(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

print("\nAdjective sentiment scores:")
total = 0
for adj in adjectives:
    score = sia.polarity_scores(adj)["compound"]
    total = total + score
    print(f"{adj:<12}{score}")

overall = total / len(adjectives)
print(f"\nOverall sentiment score: {overall:.4f} ({get_label(overall)})")

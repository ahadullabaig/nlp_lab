# 7a. Morphological analysis, and lemmatization based on the part of speech.

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download the NLTK data this program needs (skipped if already downloaded)
nltk.download("punkt", quiet=True)                           # tokenizer (old NLTK)
nltk.download("punkt_tab", quiet=True)                       # tokenizer (new NLTK)
nltk.download("averaged_perceptron_tagger", quiet=True)      # POS tagger (old NLTK)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)  # POS tagger (new NLTK)
nltk.download("wordnet", quiet=True)                         # lemmatizer dictionary
nltk.download("omw-1.4", quiet=True)                         # extra WordNet data (some NLTK versions)

text = "The children were playing happily and their mothers felt better after watching the boats."

# Morphological analysis: the POS tag tells us the form of each word
# (singular or plural, past tense, -ing form, comparative ...)
tag_meaning = {
    "NN": "noun, singular",
    "NNS": "noun, plural",
    "VB": "verb, base form",
    "VBD": "verb, past tense",
    "VBG": "verb, -ing form",
    "VBN": "verb, past participle",
    "VBZ": "verb, present (he/she/it)",
    "JJ": "adjective",
    "JJR": "adjective, comparative",
    "RB": "adverb",
    "RBR": "adverb, comparative",
}

# The lemmatizer only understands 4 POS letters, so we convert the tag
def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return "a"      # adjective
    elif tag.startswith("V"):
        return "v"      # verb
    elif tag.startswith("R"):
        return "r"      # adverb
    else:
        return "n"      # noun (the default)

lemmatizer = WordNetLemmatizer()
tagged = nltk.pos_tag(word_tokenize(text))

print(f"{'Word':<11}{'Tag':<6}{'Morphology':<27}{'Lemma (no POS)':<16}{'Lemma (with POS)':<16}")
print("-" * 76)
for word, tag in tagged:
    if word.isalpha():
        meaning = tag_meaning.get(tag, "other")
        lemma_no_pos = lemmatizer.lemmatize(word.lower())
        lemma_with_pos = lemmatizer.lemmatize(word.lower(), get_wordnet_pos(tag))
        print(f"{word:<11}{tag:<6}{meaning:<27}{lemma_no_pos:<16}{lemma_with_pos:<16}")

# Without the POS, the lemmatizer treats every word as a noun,
# so "were", "playing", "watching" and "better" are left unchanged.
# With the POS they become "be", "play", "watch" and "well".

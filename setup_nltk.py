# Run this once to download the NLTK data used by the programs.
# Both old and new package names are listed so it works on any NLTK version.

import nltk

packages = [
    "punkt", "punkt_tab",                                         # tokenizers
    "stopwords",                                                  # stop word lists
    "wordnet", "omw-1.4",                                         # lemmatizer
    "averaged_perceptron_tagger", "averaged_perceptron_tagger_eng",  # POS tagger
    "vader_lexicon",                                              # sentiment scores
]

for package in packages:
    nltk.download(package)

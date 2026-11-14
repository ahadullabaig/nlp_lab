# 3a. Compare different stemmers (Porter, Lancaster, Snowball)
#     with the WordNet lemmatizer.

from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()

words = ["running", "flies", "studies", "happily", "better",
         "generously", "caring", "wolves", "was", "fairly"]

print(f"{'Word':<12}{'Porter':<12}{'Lancaster':<12}{'Snowball':<12}{'Lemma(noun)':<13}{'Lemma(verb)':<13}")
print("-" * 74)
for w in words:
    print(f"{w:<12}{porter.stem(w):<12}{lancaster.stem(w):<12}{snowball.stem(w):<12}"
          f"{lemmatizer.lemmatize(w):<13}{lemmatizer.lemmatize(w, pos='v'):<13}")

# Observations:
# - Porter    : the classic stemmer, moderate cutting (studies -> studi).
# - Lancaster : the most aggressive, often cuts too much (generously -> gen).
# - Snowball  : an improved Porter ("Porter2"), and works for many languages.
# - Stemmers just chop off endings, so the result may not be a real word.
# - The lemmatizer looks words up in a dictionary, but it needs the right
#   part of speech: "running" stays "running" as a noun and becomes "run"
#   as a verb, and "was" wrongly becomes "wa" as a noun but correctly
#   becomes "be" as a verb (see program 7a).

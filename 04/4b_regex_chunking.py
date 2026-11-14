# 4b. Extract specific patterns (noun phrases) from a sentence using
#     regular-expression-based chunking.

import nltk
from nltk.tokenize import word_tokenize

sentence = "The little yellow dog barked at the big black cat near the old wooden house."

# Step 1: tag every word with its part of speech
tagged = nltk.pos_tag(word_tokenize(sentence))
print("POS tags:", tagged)

# Step 2: chunk grammar - a noun phrase (NP) is an optional determiner (DT),
#         any number of adjectives (JJ), then one or more nouns (NN, NNS, NNP ...)
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
parser = nltk.RegexpParser(grammar)
tree = parser.parse(tagged)
print("\nChunk tree:")
print(tree)

# Step 3: print every chunk labelled NP
print("\nNoun phrases found:")
for subtree in tree.subtrees():
    if subtree.label() == "NP":
        print(" ".join(word for word, tag in subtree.leaves()))

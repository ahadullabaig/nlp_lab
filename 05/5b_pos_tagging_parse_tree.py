# 5b. Use NLTK to process text, generate a part-of-speech tag for each word
#     and draw the parsed result.

import nltk
from nltk.tokenize import word_tokenize

text = "The quick brown fox jumps over the lazy dog."

# Step 1: tokenize and POS-tag the text
tagged = nltk.pos_tag(word_tokenize(text))

print(f"{'Word':<10}{'POS tag':<10}")
print("-" * 20)
for word, tag in tagged:
    print(f"{word:<10}{tag:<10}")

# Step 2: parse the tagged words into a tree using a chunk grammar
#         (same noun phrase grammar as program 4b)
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
parser = nltk.RegexpParser(grammar)
tree = parser.parse(tagged)

# Step 3: draw the parsed result
tree.pretty_print()   # draws the tree as text in the terminal
tree.draw()           # opens a window with the tree - close it to finish

# Note: with Tk 9, an unpatched NLTK stops at tree.draw() with
#   ValueError: invalid literal for int() with base 10: '10c'
# That is a bug inside NLTK, not in this program. The .venv on this laptop
# has the fix applied; elsewhere, the pretty_print() output shows the same tree.

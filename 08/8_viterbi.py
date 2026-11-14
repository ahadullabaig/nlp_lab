# 8. Viterbi algorithm with a Hidden Markov Model (HMM) to find the most
#    probable POS tags for the sentence "free workers".
#
# NOTE: these probabilities are made up for practice. If your class used
#       different tables, just replace the numbers below.

words = ["free", "workers"]
tags = ["ADJ", "NOUN", "VERB"]

# Start probability: P(tag) for the first word
start_prob = {"ADJ": 0.3, "NOUN": 0.4, "VERB": 0.3}

# Transition probability: P(next tag | previous tag)
# e.g. trans_prob["ADJ"]["NOUN"] = P(NOUN comes after ADJ) = 0.8
trans_prob = {
    "ADJ":  {"ADJ": 0.1, "NOUN": 0.8, "VERB": 0.1},
    "NOUN": {"ADJ": 0.1, "NOUN": 0.3, "VERB": 0.6},
    "VERB": {"ADJ": 0.3, "NOUN": 0.6, "VERB": 0.1},
}

# Emission probability: P(word | tag)
# e.g. emit_prob["NOUN"]["workers"] = P(the word is "workers" given the tag is NOUN) = 0.8
emit_prob = {
    "ADJ":  {"free": 0.5, "workers": 0.0},
    "NOUN": {"free": 0.1, "workers": 0.8},
    "VERB": {"free": 0.4, "workers": 0.1},
}

# table[t][tag] = probability of the best tag sequence that ends with `tag` at word t
# back[t][tag]  = the tag of the previous word on that best sequence
table = [{} for word in words]
back = [{} for word in words]

# Step 1: first word -> start probability x emission probability
for tag in tags:
    table[0][tag] = start_prob[tag] * emit_prob[tag][words[0]]
    back[0][tag] = None

# Step 2: every next word -> best (previous value x transition) x emission
for t in range(1, len(words)):
    for tag in tags:
        best_prob = 0
        best_prev = None
        for prev in tags:
            prob = table[t - 1][prev] * trans_prob[prev][tag]
            if prob > best_prob:
                best_prob = prob
                best_prev = prev
        table[t][tag] = best_prob * emit_prob[tag][words[t]]
        back[t][tag] = best_prev

# Step 3: print the Viterbi table
print(f"{'Word':<10}", end="")
for tag in tags:
    print(f"{tag:<10}", end="")
print()
for t in range(len(words)):
    print(f"{words[t]:<10}", end="")
    for tag in tags:
        print(f"{table[t][tag]:<10.4f}", end="")
    print()

# Step 4: the best tag for the last word is the one with the highest value
last_tag = tags[0]
for tag in tags:
    if table[-1][tag] > table[-1][last_tag]:
        last_tag = tag

# Step 5: follow the back pointers from the last word to the first
best_tags = [last_tag]
for t in range(len(words) - 1, 0, -1):
    best_tags.insert(0, back[t][best_tags[0]])

print("\nMost probable tags:")
for word, tag in zip(words, best_tags):
    print(f"{word:<10}{tag}")
print(f"Probability: {table[-1][last_tag]:.4f}")

# Worked by hand (same numbers as above):
#   Word 1 "free":
#     ADJ  = 0.3 x 0.5 = 0.15
#     NOUN = 0.4 x 0.1 = 0.04
#     VERB = 0.3 x 0.4 = 0.12
#   Word 2 "workers":
#     NOUN = max(0.15 x 0.8, 0.04 x 0.3, 0.12 x 0.6) x 0.8 = 0.12 x 0.8 = 0.096   (came from ADJ)
#     VERB = max(0.15 x 0.1, 0.04 x 0.6, 0.12 x 0.1) x 0.1 = 0.024 x 0.1 = 0.0024 (came from NOUN)
#     ADJ  = max(0.15 x 0.1, 0.04 x 0.1, 0.12 x 0.3) x 0.0 = 0                    (came from VERB)
#   Highest value for the last word = NOUN (0.096), and it came from ADJ
#   Answer: free/ADJ  workers/NOUN

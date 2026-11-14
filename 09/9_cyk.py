# 9. CYK (Cocke-Younger-Kasami) algorithm: decide whether a given string
#    belongs to the language of a grammar.
#
# The grammar must be in Chomsky Normal Form (CNF), so every rule is either
#   A -> B C    (two non-terminals)   or   A -> word   (one terminal)

grammar = [
    ("S", ["NP", "VP"]),
    ("NP", ["Det", "N"]),
    ("VP", ["V", "NP"]),
    ("Det", ["the"]),
    ("Det", ["a"]),
    ("N", ["dog"]),
    ("N", ["cat"]),
    ("N", ["man"]),
    ("V", ["chased"]),
    ("V", ["saw"]),
]

print("Grammar:")
for lhs, rhs in grammar:
    print(f"  {lhs} -> {' '.join(rhs)}")

sentence = input("\nEnter a sentence: ")
words = sentence.lower().split()
n = len(words)

# table[i][j] = set of non-terminals that can produce words[i] ... words[j]
table = [[set() for j in range(n)] for i in range(n)]

# Step 1: fill the diagonal (single words) using rules A -> word
for i in range(n):
    for lhs, rhs in grammar:
        if rhs == [words[i]]:
            table[i][i].add(lhs)

# Step 2: fill longer spans using rules A -> B C
for length in range(2, n + 1):               # length of the span
    for i in range(n - length + 1):          # where the span starts
        j = i + length - 1                   # where the span ends
        for k in range(i, j):                # split into words[i..k] and words[k+1..j]
            for lhs, rhs in grammar:
                if len(rhs) == 2 and rhs[0] in table[i][k] and rhs[1] in table[k + 1][j]:
                    table[i][j].add(lhs)

# Step 3: print the CYK table (row = first word of the span, column = last word)
print(f"\n{'':<10}", end="")
for word in words:
    print(f"{word:<10}", end="")
print()
for i in range(n):
    print(f"{words[i]:<10}", end="")
    for j in range(n):
        if j < i:
            cell = ""
        elif table[i][j]:
            cell = ",".join(sorted(table[i][j]))
        else:
            cell = "-"
        print(f"{cell:<10}", end="")
    print()

# Step 4: the string is in the language if S can produce the whole string
if "S" in table[0][n - 1]:
    print("\nThe string BELONGS to the language of the grammar.")
else:
    print("\nThe string does NOT belong to the language of the grammar.")

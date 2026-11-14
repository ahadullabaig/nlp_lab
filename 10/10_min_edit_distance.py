# 10. Minimum edit distance from a source string to a target string using
#     dynamic programming. Insertion = 1, deletion = 1, substitution = 1.
#     Try: intention -> execution (answer 5),  Piece -> Peace (answer 2)

source = input("Enter the source string: ")
target = input("Enter the target string: ")

n = len(source)
m = len(target)

# table[i][j] = edit distance between the first i letters of source
#               and the first j letters of target
table = [[0] * (m + 1) for i in range(n + 1)]

# Step 1: first column and first row
for i in range(n + 1):
    table[i][0] = i          # delete all i letters
for j in range(m + 1):
    table[0][j] = j          # insert all j letters

# Step 2: fill the rest of the table
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if source[i - 1] == target[j - 1]:
            sub_cost = 0     # letters match, nothing to change
        else:
            sub_cost = 1
        table[i][j] = min(table[i - 1][j] + 1,              # deletion
                          table[i][j - 1] + 1,              # insertion
                          table[i - 1][j - 1] + sub_cost)   # substitution

# Step 3: print the table ("#" stands for the empty string)
print(f"\n{'':<4}{'#':<4}", end="")
for letter in target:
    print(f"{letter:<4}", end="")
print()
for i in range(n + 1):
    if i == 0:
        label = "#"
    else:
        label = source[i - 1]
    print(f"{label:<4}", end="")
    for j in range(m + 1):
        print(f"{table[i][j]:<4}", end="")
    print()

print(f"\nMinimum edit distance from '{source}' to '{target}' = {table[n][m]}")

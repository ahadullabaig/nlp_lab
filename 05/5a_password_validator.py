# 5a. Validate a password entered by the user. It must have:
#     at least 8 characters, an uppercase letter, a lowercase letter,
#     a digit and a special character.

import re

password = input("Enter a password: ")

problems = []
if len(password) < 8:
    problems.append("at least 8 characters")
if not re.search(r"[A-Z]", password):
    problems.append("at least one uppercase letter (A-Z)")
if not re.search(r"[a-z]", password):
    problems.append("at least one lowercase letter (a-z)")
if not re.search(r"[0-9]", password):
    problems.append("at least one digit (0-9)")
if not re.search(r"[^A-Za-z0-9]", password):     # anything that is not a letter or digit
    problems.append("at least one special character (@, #, $, %, &, * ...)")

if problems:
    print("Invalid password. It must contain:")
    for problem in problems:
        print(" -", problem)
else:
    print("Valid password.")

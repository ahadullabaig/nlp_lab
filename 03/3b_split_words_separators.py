# 3b. Split a string of words separated by commas and spaces into two lists:
#     words and separators.

import re

text = "The colors in my studyroom are blue, green, and yellow."

words = re.findall(r"[^,\s]+", text)       # runs of characters that are not a comma or space
separators = re.findall(r",\s|\s", text)   # a comma followed by a space, or just a space

print([words, separators])

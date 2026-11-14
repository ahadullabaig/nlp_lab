# 4a. Use a regular expression to simulate a Finite State Automaton (FSA)
#     that recognizes sheeptalk.
#
# Sheeptalk is: b, then two or more a's, then !   ->  baa!  baaa!  baaaaa! ...
#
#   q0 --b--> q1 --a--> q2 --a--> q3 --!--> q4 (final state)
#                                 q3 --a--> q3  (loop: any number of extra a's)
#
# The regex  baa+!  is exactly this FSA:
#   b   ->  q0 to q1
#   a   ->  q1 to q2
#   a+  ->  q2 to q3, then the loop on q3 for every extra a
#   !   ->  q3 to q4

import re

def is_sheeptalk(string):
    # fullmatch: the WHOLE string must match, like an FSA ending in the final state
    return re.fullmatch(r"baa+!", string) is not None


tests = ["baa!", "baaa!", "baaaaaa!", "ba!", "baa", "abaa!", "baa!x", "b!"]
for s in tests:
    if is_sheeptalk(s):
        print(f"{s:<10} -> Accepted")
    else:
        print(f"{s:<10} -> Rejected")

s = input("\nEnter a string to check: ")
if is_sheeptalk(s):
    print(f"{s} -> Accepted")
else:
    print(f"{s} -> Rejected")

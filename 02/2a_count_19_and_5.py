# 2a. Return True if a list has exactly two 19s and at least three 5s,
#     otherwise return False.

def check_list(numbers):
    return numbers.count(19) == 2 and numbers.count(5) >= 3


# The three sample inputs from the question
print(check_list([19, 19, 15, 5, 3, 5, 5, 2]))   # True
print(check_list([19, 15, 15, 5, 3, 3, 5, 2]))   # False
print(check_list([19, 19, 5, 5, 5, 5, 5]))       # True

# Create your own list with n values
n = int(input("\nHow many numbers? "))
numbers = []
for i in range(n):
    numbers.append(int(input(f"Enter number {i + 1}: ")))

print("List:", numbers)
print("Result:", check_list(numbers))

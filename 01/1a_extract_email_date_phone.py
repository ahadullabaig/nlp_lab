# 1a. Extract email addresses, dates and phone numbers from a text file
#     using Python regular expressions.

import re

# Step 1: read the whole text file into one string
with open("sample.txt") as file:
    text = file.read()

# Step 2: one pattern for each thing we want to find
email_pattern = r"[\w.]+@[\w.]+\.\w+"             # name@domain.com
date_pattern = r"\d{1,2}[/-]\d{1,2}[/-]\d{4}"     # 15/03/2025 or 10-03-2025
phone_pattern = r"\+91[- ]?\d{10}|\b\d{10}\b"     # +91 9876543210 or 9123456780
# \b means "word boundary", so we never grab 10 digits out of a longer number

# Step 3: re.findall returns a list of every match in the text
emails = re.findall(email_pattern, text)
dates = re.findall(date_pattern, text)
phones = re.findall(phone_pattern, text)

print("Emails:", emails)
print("Dates :", dates)
print("Phones:", phones)

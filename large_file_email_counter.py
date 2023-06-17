"""Script that counts the unique email addresses in a larger file.
Reads the file line by line to avoid occasional memory crash."""

import re

# Function to read a file line by line and count the number of email addresses
def count_emails(file_path):
    email_pattern = r'((?:[a-zA-Z0-9_+&*-]*(?:\.[a-zA-Z0-9_+&*-]*)*)@(?:(?:[a-zA-Z0-9-]*\.)*[a-zA-Z]{2,17}))'  # Regex pattern for matching email addresses
    emails = set()  # Set to store unique email addresses
    with open(file_path, 'r', errors="ignore", encoding="utf-8") as file:
        for line in file:
            matches = re.findall(email_pattern, line)  # Find all email addresses in the line
            for match in matches:
                emails.add(match)  # Add unique email addresses to the set
    return len(emails)  # Return the number of unique email addresses


# Ask for the file path
file_path = input('Enter the file path: ')

# Call the function to count the email addresses
num_emails = count_emails(file_path)

# Print the result
print(f'The number of unique email addresses in the file is {num_emails:,d}.')

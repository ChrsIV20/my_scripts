# Script that counts the unique email addresses in a file.

import re
from tqdm import tqdm

# Define the regular expression pattern to match email addresses
email_regex = r"((?:[a-zA-Z0-9_+&*-]*(?:\.[a-zA-Z0-9_+&*-]*)*)@(?:(?:[a-zA-Z0-9-]*\.)*[a-zA-Z]{2,17}))"
input_file = input("Give me file path: ")

# Open the text file for reading
with open(input_file, 'r', errors="ignore", encoding="utf-8") as f:
    # Read the file contents into a string
    file_contents = f.read()

    # Use the regular expression pattern to find all email addresses in the string
    matches = re.findall(email_regex, file_contents)

    unique_matches = set(matches)
    num_matches = len(matches)

    # Create a progress bar to show the progress of the matching process
    with tqdm(total=num_matches, initial=0) as pbar:
        for match in re.finditer(email_regex, file_contents):
            # Process each match as before (e.g. extract data, write to file, etc.)
            pbar.update(1)

    # Count the number of unique email addresses
    num_unique_emails = len(unique_matches)

    # Print the number of unique email addresses
    print(f"Found {num_unique_emails:,d} unique email addresses.")


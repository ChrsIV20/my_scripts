# Script that converts all .xls or .xlsx files in a given folder to .csv

import os
import pandas as pd

# Set the directory path to the folder containing the .xls and .xlsx files
directory = input("Give me directory path: ")

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .xls or .xlsx file
    if filename.endswith(".xls") or filename.endswith(".xlsx"):
        # Read the Excel file into a pandas DataFrame
        if filename.endswith(".xls"):
            df = pd.read_excel(os.path.join(directory, filename), engine='xlrd')
        elif filename.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(directory, filename))

        # Example: Save the modified DataFrame to a new file with .csv extension
        new_filename = os.path.splitext(filename)[0] + ".csv"
        df.to_csv(os.path.join(directory, new_filename), index=False)

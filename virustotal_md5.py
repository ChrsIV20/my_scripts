# Script that allows MD5 hash analysis with VirusTotal from the terminal.

import re
import vt

# Prompt for the API key
api_key = "02c6255a76b254eec4be1d50cd071556fd424ccf1b28985959e32d5fc7844d11"

# Create a VirusTotal API client
client = vt.Client(api_key)

# Prompt for the file hashes
file_hashes = input("Enter the file hashes (separated by commas): ").split(',')

# Regular expression pattern for MD5 hash format
md5_pattern = re.compile(r"^[a-fA-F0-9]{32}$")

# Scan each file hash
for file_hash in file_hashes:
    file_hash = file_hash.strip()

    # Check if the hash is valid
    if not md5_pattern.match(file_hash):
        print(f"Invalid hash: {file_hash}")
        continue

    try:
        # Retrieve the file report
        file_report = client.get_object("/files/{}".format(file_hash))

        # Print the scan results
        print(f"Scan results for file hash: {file_hash}")
        if file_report.last_analysis_results:
            for engine, result in file_report.last_analysis_results.items():
                print(f"{engine}: {result['result']}")
        else:
            print("No scan results available")
        print()

    except vt.APIError as e:
        print(f"Error occurred for file hash: {file_hash}")
        print(f"Error message: {e}")
        print()

# Close the VirusTotal API client
client.close()

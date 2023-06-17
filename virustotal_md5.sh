#!/bin/bash

# Replace <YOUR_API_KEY> with your VirusTotal API key
API_KEY="02c6255a76b254eec4be1d50cd071556fd424ccf1b28985959e32d5fc7844d11"

# Prompt for the MD5 hash
read -p "Enter the MD5 hash: " MD5_HASH

# Submit the file for analysis
RESPONSE=$(curl --request GET \
                --url "https://www.virustotal.com/api/v3/files/$MD5_HASH" \
                --header "x-apikey: $API_KEY")

# Print the analysis results
echo $RESPONSE | jq '.data.attributes.last_analysis_results'



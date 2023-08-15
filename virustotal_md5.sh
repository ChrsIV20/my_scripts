#!/bin/bash

# Replace <YOUR_API_KEY> with your VirusTotal API key
API_KEY="<YOUR_API_KEY>"

# Prompt for the MD5 hash
read -p "Enter the MD5 hash: " MD5_HASH

# Submit the file for analysis
RESPONSE=$(curl --request GET \
                --url "https://www.virustotal.com/api/v3/files/$MD5_HASH" \
                --header "x-apikey: $API_KEY")

# Print the analysis results
echo $RESPONSE | jq '.data.attributes.last_analysis_results'



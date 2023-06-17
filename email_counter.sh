#!/bin/bash

echo "Enter the file path: "
read file_path

md5_hash=$(md5sum "$file_path" | awk '{print $1}')
echo "MD5 hash of the file: $md5_hash"

uniq_emails=$(grep -oE "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" "$file_path" | sort | uniq -c | wc -l | awk '{print $1}' | numfmt --grouping)
echo "Total unique email addresses in the file: $uniq_emails"

echo "Do you want to print 10 random emails from the file? (y/n)"
read choice

if [[ $choice == "y" ]]; then
    echo "Random email addresses:"
    grep -oE "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" "$file_path" | shuf -n 10
fi

echo "Do you want to scan for unique phone numbers? (y/n)"
read choice

if [[ $coice == "y" ]]; then
    echo "Total unique phone numbers in the file:"
    grep -oE "\b\d{9,11}\b" "$file_path" | sort | uniq -c | wc -l | awk '{print $1}' | numfmt --grouping
fi


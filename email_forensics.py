"""Script that parses .eml files for further investigation about the sender and such,
also it extracts the attachments.""" 

import os
import email
import argparse

# Function to parse EML file
def parse_eml(file_path, save_dir):
    try:
        with open(file_path, 'r') as eml_file:
            eml_message = email.message_from_file(eml_file)

        print(f"Subject: {eml_message['Subject']}")
        print(f"From: {eml_message['From']}")
        print(f"To: {eml_message['To']}")
        print(f"CC: {eml_message['Cc']}")
        print(f"Date: {eml_message['Date']}")

        attachments = []
        for part in eml_message.walk():
            if part.get_content_disposition() == 'attachment':
                attachment_filename = part.get_filename()
                if attachment_filename:
                    attachment_path = os.path.join(save_dir, attachment_filename)
                    with open(attachment_path, 'wb') as attachment_file:
                        attachment_file.write(part.get_payload(decode=True))
                    attachments.append(attachment_filename)

        if attachments:
            print("Attachments:")
            for attachment in attachments:
                print(f"\t{attachment}")
        else:
            print("No attachments found.")

        print("\n")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Email Parser")
    parser.add_argument('file', help="Path to the EML file")
    parser.add_argument('-d', '--dir', help="Directory to save attachments", default='attachments')
    args = parser.parse_args()

    file_path = args.file
    save_dir = args.dir

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    parse_eml(file_path, save_dir)


if __name__ == '__main__':
    main()

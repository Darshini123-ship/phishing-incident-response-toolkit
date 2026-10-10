import re

def parse_email_header(header_file_path):
    """
    Parses a raw email header file to extract vital triage details:
    Sender, Reply-To, Return-Path, and Subject.
    """
    try:
        with open(header_file_path, 'r') as file:
            header_content = file.read()
    except FileNotFoundError:
        print(f"Error: {header_file_path} not found.")
        return

    print("--- Phishing Email Header Analysis ---")
    
    # Simple regex extractions
    from_match = re.search(r"^From:\s*(.*)$", header_content, re.MULTILINE)
    reply_to_match = re.search(r"^Reply-To:\s*(.*)$", header_content, re.MULTILINE)
    subject_match = re.search(r"^Subject:\s*(.*)$", header_content, re.MULTILINE)
    return_path_match = re.search(r"^Return-Path:\s*(.*)$", header_content, re.MULTILINE)

    print(f"From       : {from_match.group(1) if from_match else 'Not Found'}")
    print(f"Reply-To   : {reply_to_match.group(1) if reply_to_match else 'Not Found (Matches From)'}")
    print(f"Return-Path: {return_path_match.group(1) if return_path_match else 'Not Found'}")
    print(f"Subject    : {subject_match.group(1) if subject_match else 'Not Found'}")
    print("--------------------------------------")

if __name__ == "__main__":
    parse_email_header("sample_header.txt")

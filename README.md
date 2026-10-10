 # Phishing Incident Response & Header Parsing Toolkit

## Objective
A lightweight Python automation utility designed to streamline the initial triage phase of phishing email investigations by rapidly parsing raw headers to detect spoofing indicators, mismatching return paths, and deceptive reply-to addresses.

## Features
* **Automated Extraction:** Parses raw email text files using regular expressions to extract critical routing and sender attributes.
* **Spoofing Indicator Detection:** Quickly highlights discrepancies between the `From` address, `Return-Path`, and `Reply-To` fields—common tactics used in social engineering attacks.
* **NIST-Aligned Triage:** Accelerates the detection phase of the Incident Response lifecycle.

## How to Run
1. Place your raw email headers into a text file (e.g., `sample_header.txt`).
2. Run the script:
   ```bash
   python scripts/email_header_parser.py

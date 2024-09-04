import pyperclip
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Copy content from a specified line in clipboard.txt to the clipboard')
parser.add_argument('-n', type=int, required=True, help='Line number to retrieve content from (1-5)')
args = parser.parse_args()

# Validate line number and read the content from the specified line
if 1 <= args.n <= 5:
    with open('clipboard.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) >= args.n:
            # Copy the specific line, stripped of any trailing newlines, to the clipboard
            content_to_copy = lines[args.n - 1].strip()
            pyperclip.copy(content_to_copy)
            print(f"Copied content from line {args.n} to clipboard: '{content_to_copy}'")
        else:
            print(f"Error: Line {args.n} is empty or does not exist.")
else:
    print("Error: Line number must be between 1 and 5.")

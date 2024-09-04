import pyperclip
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Copy clipboard content to a specified line in clipboard.txt')
parser.add_argument('-n', type=int, required=True, help='Line number to store clipboard content (1-5)')
args = parser.parse_args()

# Read the clipboard content and strip extra newlines
clipboard_content = pyperclip.paste().strip()

# Validate line number
if 1 <= args.n <= 5:
    with open('clipboard.txt', 'r+') as file:
        lines = file.readlines()
        # Ensure there are exactly 5 lines in the file
        while len(lines) < 5:
            lines.append("\n")
        
        # Update the specific line, removing any extra newlines
        lines[args.n - 1] = clipboard_content + "\n"
        
        # Write the updated lines back to the file
        file.seek(0)
        file.writelines(lines)
        file.truncate()  # Ensure no trailing lines
else:
    print("Error: Line number must be between 1 and 5.")

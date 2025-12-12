# Write your code here
import re

def remove_repeated_words(string: str) -> str:
    """Remove consecutive duplicated words from string."""
    return re.sub(r'(\b\w+\b)(\s+\1)+', r'\1', string)

# Write your code here
import re

def only_vowels(string):
    """Return True if string consists of one or more repetitions of 'abc'."""
    pattern = r"^(a|e|o|i|u)*$"

    return re.fullmatch(pattern, string) is not None

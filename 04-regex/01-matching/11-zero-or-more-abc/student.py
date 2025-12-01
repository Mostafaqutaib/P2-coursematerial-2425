# Write your code here
import re

def zero_or_more_abc(string):
    """Return True if string consists of one or more repetitions of 'abc'."""
    pattern = r"^(abc)*$"
    return re.fullmatch(pattern, string) is not None

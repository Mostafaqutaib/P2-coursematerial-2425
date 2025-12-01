# Write your code here
import re

def abc_or_xyz(string):
    """Return True if string consists of one or more repetitions of 'abc'."""
    pattern = r"^(abc|xyz)$"

    return re.fullmatch(pattern, string) is not None

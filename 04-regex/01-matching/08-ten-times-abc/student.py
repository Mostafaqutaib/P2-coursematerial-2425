# Write your code here
import re

def ten_times_abc(string):
    """Return True if string consists of one or more repetitions of 'abc'."""
    pattern = r"^(abc){10}$"
    return re.fullmatch(pattern, string) is not None
# Write your code here

# Write your code here
# Write your code here
import re

def three_to_ten_times_abc(string):
    """Return True if string consists of one or more repetitions of 'abc'."""
    pattern = r"^(abc){3,10}$"
    return re.fullmatch(pattern, string) is not None

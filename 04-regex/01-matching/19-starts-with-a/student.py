# Write your code here
import re

def starts_with_a(string):
    pattern = r'a'
    if re.match(pattern, string):
        return True
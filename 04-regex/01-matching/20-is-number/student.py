# Write your code here
import re

def is_number(string):
    pattern = r'^\d+(\.\d+)?$'
    if re.fullmatch(pattern, string):
        return True
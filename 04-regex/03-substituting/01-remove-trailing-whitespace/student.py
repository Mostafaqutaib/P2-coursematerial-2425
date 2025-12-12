# Write your code here
import re 

def remove_trailing_whitespace(string):
    match = re.sub(r'[ \t]+$','',string, flags=re.MULTILINE)
    return match
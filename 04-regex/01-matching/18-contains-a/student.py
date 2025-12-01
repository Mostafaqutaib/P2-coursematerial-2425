# Write your code here
import re
def contains_a(string):
    pattern = r'(a)*'
    if re.search(pattern, string):
        return True
# Write your code here
import re
def equals_b(string):
    if re.fullmatch('b', string):
        return True
    else:
        return False
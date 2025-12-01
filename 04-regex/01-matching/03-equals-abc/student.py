# Write your code here
import re

def equals_abc(string):
    if re.fullmatch('abc', string):
        return True
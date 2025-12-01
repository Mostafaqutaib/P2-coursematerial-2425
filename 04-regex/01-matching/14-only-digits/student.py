# Write your code here
import re

def only_digits(string):
    patteren = r'^[0123456789]*$'
    if re.fullmatch(patteren, string):
        return True
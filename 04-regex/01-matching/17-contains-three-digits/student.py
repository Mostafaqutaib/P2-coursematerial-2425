
# Write your code here
# Write your code here
import re

def contains_three_digits(string):
    patteren = r".*[0-9].*[0-9].*[0-9].*"

    if re.fullmatch(patteren, string):
        return True
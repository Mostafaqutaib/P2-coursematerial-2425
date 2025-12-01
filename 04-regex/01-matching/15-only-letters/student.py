
# Write your code here
import re

def only_letters(string):
    patteren = r'^[a-z|A-Z]*$'
    if re.fullmatch(patteren,string):
        return True
# Write your code here
import re
def equals_a(string):
    if re.fullmatch('^a', string):
        return True
    else:
        return False

    
blabla = equals_a("bla bla o la la")

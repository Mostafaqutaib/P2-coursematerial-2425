# Write your code here
import re

def is_dna(string):
    patteren = r"^[GATC]*$"
    if re.fullmatch(patteren, string):
        return True
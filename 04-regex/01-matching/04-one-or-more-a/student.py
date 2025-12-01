# Write your code here
import re


def one_or_more_a(string):
    if re.fullmatch('a+', string):
        return True
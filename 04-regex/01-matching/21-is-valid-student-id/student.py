# Write your code here
import re

def is_valid_student_id(string):
    if re.fullmatch(r'^[rRsS]\d{7}$',string):
        return True
    
    #studentid == r1234567 or Q0000000
import re

def is_valid_password(string: str) -> bool:
    """Return True if the password meets all complexity requirements."""
    pattern = (
        r'^(?=.*[0-9])'          # at least one digit
        r'(?=.*[a-z])'           # at least one lowercase
        r'(?=.*[A-Z])'           # at least one uppercase
        r'(?=.*[+\-*/\.@])'      # at least one special character
        r'(?!.*(.).*\1.*\1.*\1)' # no character repeated 4 times anywhere
        r'(?!.*(.)\2\2)'         # no 3 identical chars in a row
        r'.{12,}$'               # minimum length 12
    )
    return re.fullmatch(pattern, string) 

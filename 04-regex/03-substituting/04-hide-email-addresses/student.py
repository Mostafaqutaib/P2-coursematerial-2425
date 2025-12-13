import re

def hide_email_addresses(string: str) -> str:
    """Replace all email addresses by asterisks of equal length."""
    
    def replace(match):
        email = match.group()
        return '*' * len(email)
    
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]+'
    return re.sub(pattern, replace, string)

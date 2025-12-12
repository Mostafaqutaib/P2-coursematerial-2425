# Write your code here
import re

def scrape_email_addresses(string):
    match = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]+',string)
    return match
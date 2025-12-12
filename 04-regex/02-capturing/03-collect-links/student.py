# Write your code here
import re
def collect_links(string):
    match = re.findall(r'<a href="([^"]*)">', string)
    return match
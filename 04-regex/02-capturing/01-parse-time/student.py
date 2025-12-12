import re


def parse_time(string: str):
    """Return a tuple (hours, minutes, seconds, milliseconds) parsed from string,
    or None if string is not a valid time format."""
    
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)
    if not match:
        return None
    
    h, m, s, ms = match.groups('.000')   # default milliseconds if missing
    
    # ms looks like ".123", so remove the leading dot
    ms_int = int(ms[1:])
    return int(h), int(m), int(s), ms_int
        
        
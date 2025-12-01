import re

def one_or_more_abc(string: str) -> bool:
    """Return True if string consists of one or more repetitions of 'abc'."""
    pattern = r"^(abc)+$"
    return re.fullmatch(pattern, string) is not None

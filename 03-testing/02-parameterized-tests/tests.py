import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string', [
    ('((((()))))'),
    ('()(()()())'),
    ('((((((()))))))')])
def test_matching_parentheses_true(string):
    assert matching_parentheses(string), f"parenttheses {string}  match"

@pytest.mark.parametrize('string', [

    ('('),
    (')'),
    ('(()'),
    ('((()))(()()')
] )
def test_matching_parentheses_false(string):
    assert not matching_parentheses(string), f"parenttheses {string} one or more no match"
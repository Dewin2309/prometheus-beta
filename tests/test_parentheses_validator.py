import pytest
from src.parentheses_validator import is_valid_parentheses

def test_empty_string():
    """Test that an empty string is considered valid."""
    assert is_valid_parentheses("") == True

def test_simple_valid_parentheses():
    """Test basic valid parentheses combinations."""
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("(())") == True
    assert is_valid_parentheses("()()") == True

def test_nested_valid_parentheses():
    """Test nested valid parentheses combinations."""
    assert is_valid_parentheses("((()))") == True
    assert is_valid_parentheses("(()())") == True

def test_invalid_parentheses():
    """Test invalid parentheses combinations."""
    assert is_valid_parentheses("(") == False
    assert is_valid_parentheses(")") == False
    assert is_valid_parentheses(")(") == False
    assert is_valid_parentheses("((()") == False
    assert is_valid_parentheses("())") == False

def test_unbalanced_parentheses():
    """Test unbalanced parentheses scenarios."""
    assert is_valid_parentheses("((()))()") == True
    assert is_valid_parentheses("(())(()") == False

def test_long_valid_sequence():
    """Test a long, valid parentheses sequence."""
    long_valid = "(" * 1000 + ")" * 1000
    assert is_valid_parentheses(long_valid) == True

def test_long_invalid_sequence():
    """Test a long, invalid parentheses sequence."""
    long_invalid_1 = "(" * 1000 + ")" * 999
    long_invalid_2 = ")" * 1000 + "(" * 1000
    
    assert is_valid_parentheses(long_invalid_1) == False
    assert is_valid_parentheses(long_invalid_2) == False
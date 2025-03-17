import pytest
from src.palindrome_checker import is_palindrome_number

def test_palindrome_number_positive():
    """Test positive palindrome numbers."""
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(1) == True

def test_palindrome_number_negative():
    """Test non-palindrome numbers."""
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(10) == False
    assert is_palindrome_number(1234) == False

def test_negative_numbers():
    """Test that negative numbers are not palindromes."""
    assert is_palindrome_number(-121) == False
    assert is_palindrome_number(-11) == False

def test_type_errors():
    """Test type error handling."""
    with pytest.raises(TypeError):
        is_palindrome_number("121")
    
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    
    with pytest.raises(TypeError):
        is_palindrome_number(None)
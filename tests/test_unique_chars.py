import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_basic():
    """Test basic functionality of extracting unique characters."""
    assert extract_unique_chars("123456789") == "123456789"
    assert extract_unique_chars("1112223334444") == "1234"

def test_extract_unique_chars_mixed():
    """Test with mixed numeric characters."""
    assert extract_unique_chars("1232145679") == "12345679"

def test_extract_unique_chars_edge_cases():
    """Test edge cases."""
    assert extract_unique_chars("") == ""
    assert extract_unique_chars("0000") == "0"

def test_extract_unique_chars_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        extract_unique_chars(12345)
    
    with pytest.raises(TypeError):
        extract_unique_chars(None)

def test_extract_unique_chars_non_numeric():
    """Test behavior with non-numeric characters."""
    assert extract_unique_chars("12a34b56c") == "123456"
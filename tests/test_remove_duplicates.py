import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbcc") == "abc"

def test_remove_duplicates_empty_string():
    """Test empty string input."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicates_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicates_all_duplicates():
    """Test string with all duplicate characters."""
    assert remove_duplicate_chars("aaaaa") == "a"

def test_remove_duplicates_mixed_duplicates():
    """Test string with mixed duplicate patterns."""
    assert remove_duplicate_chars("abracadabra") == "abrcd"

def test_remove_duplicates_invalid_input():
    """Test that non-lowercase input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars("Hello")
    
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars("ABC123")
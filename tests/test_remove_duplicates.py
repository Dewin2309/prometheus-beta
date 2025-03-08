import pytest
from src.remove_duplicates import remove_duplicates_over_two

def test_remove_duplicates_over_two_multiple_duplicates():
    """Test removing multiple duplicates."""
    assert remove_duplicates_over_two("aabbbcccc") == "aabbcc"

def test_remove_duplicates_over_two_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicates_over_two("python") == "python"

def test_remove_duplicates_over_two_empty_string():
    """Test empty string input."""
    assert remove_duplicates_over_two("") == ""

def test_remove_duplicates_over_two_all_removed():
    """Test case where all characters would be removed."""
    assert remove_duplicates_over_two("aaaa") == "aa"

def test_remove_duplicates_over_two_mixed_cases():
    """Test mixed case with some characters repeated."""
    assert remove_duplicates_over_two("aabbccdddd") == "aabbccdd"

def test_remove_duplicates_over_two_special_characters():
    """Test with special characters and mixed repetitions."""
    assert remove_duplicates_over_two("!!@@##$$$") == "!!@@##$$"

def test_remove_duplicates_over_two_unicode():
    """Test with Unicode characters."""
    assert remove_duplicates_over_two("🌞🌞🌞🌟🌟") == "🌞🌞🌟🌟"
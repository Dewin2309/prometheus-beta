import pytest
from src.longest_unique_substring import longest_unique_substring

def test_typical_cases():
    """Test typical use cases with varied input strings."""
    assert longest_unique_substring("abcabcbb") == 3  # 'abc'
    assert longest_unique_substring("bbbbb") == 1     # 'b'
    assert longest_unique_substring("pwwkew") == 3    # 'wke'

def test_edge_cases():
    """Test edge cases like empty string, single character, etc."""
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("a") == 1
    assert longest_unique_substring("aab") == 2       # 'ab'
    assert longest_unique_substring("dvdf") == 3      # 'vdf'

def test_complex_cases():
    """Test more complex scenarios with different unique substring patterns."""
    assert longest_unique_substring("abcdefg") == 7   # entire string unique
    assert longest_unique_substring("abba") == 2      # 'ab' or 'ba'
    assert longest_unique_substring("tmmzuxt") == 5   # 'mzuxt'

def test_non_ascii_characters():
    """Test with non-ASCII characters to ensure full Unicode support."""
    assert longest_unique_substring("こんにちは") == 5
    assert longest_unique_substring("🌈🌟🌈") == 2

def test_whitespace_and_special_characters():
    """Test with strings containing whitespace and special characters."""
    assert longest_unique_substring("  a b c  ") == 3
    assert longest_unique_substring("!@#$%^&*()") == 10
    assert longest_unique_substring("a!b@c#") == 6
import pytest
from src.substring_generator import generate_all_substrings

def test_generate_all_substrings_normal_case():
    """Test generating substrings for a typical string."""
    result = generate_all_substrings("abc")
    assert set(result) == set(['a', 'ab', 'abc', 'b', 'bc', 'c'])
    assert len(result) == 6

def test_generate_all_substrings_empty_string():
    """Test generating substrings for an empty string."""
    result = generate_all_substrings("")
    assert result == []

def test_generate_all_substrings_single_char():
    """Test generating substrings for a single character string."""
    result = generate_all_substrings("x")
    assert result == ['x']

def test_generate_all_substrings_repeated_chars():
    """Test generating substrings for a string with repeated characters."""
    result = generate_all_substrings("aaa")
    assert set(result) == set(['a', 'aa', 'aaa'])

def test_generate_all_substrings_long_string():
    """Test generating substrings for a longer string."""
    input_str = "python"
    result = generate_all_substrings(input_str)
    
    # Verify length of result
    expected_len = (len(input_str) * (len(input_str) + 1)) // 2
    assert len(result) == expected_len
    
    # Verify each substring
    for substring in result:
        assert substring in input_str
        assert len(substring) <= len(input_str)

def test_generate_all_substrings_unicode():
    """Test generating substrings for a string with unicode characters."""
    result = generate_all_substrings("こんにちは")
    assert len(result) > 0
    
    # Verify each substring is part of the original string
    for substring in result:
        assert substring in "こんにちは"
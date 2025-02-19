import pytest
from src.palindrome_substrings import find_non_overlapping_palindromes

def test_find_non_overlapping_palindromes():
    # Test empty string
    assert find_non_overlapping_palindromes("") == []
    
    # Test single character
    assert find_non_overlapping_palindromes("a") == ["a"]
    
    # Test simple palindrome
    assert find_non_overlapping_palindromes("racecar") == ["a", "aceca", "c", "e", "r", "racecar"]
    
    # Test string with multiple palindromes
    assert find_non_overlapping_palindromes("aabaa") == ["a", "aa", "aba"]
    
    # Test string with no palindromes except single characters
    assert find_non_overlapping_palindromes("abcd") == ["a", "b", "c", "d"]
    
    # Test mixed case palindromes
    assert find_non_overlapping_palindromes("AbBa") == ["A", "B", "a", "b", "bB"]
    
    # Test long palindrome
    result = find_non_overlapping_palindromes("abaxyzzyxf")
    assert "aba" in result
    assert "xyz" in result
    assert "zyzz" in result
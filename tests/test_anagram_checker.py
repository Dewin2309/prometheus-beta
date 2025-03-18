import pytest
from src.anagram_checker import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios."""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True

def test_case_insensitive():
    """Verify the function is case-insensitive."""
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("SILENT", "listen") == True

def test_whitespace_handling():
    """Check that whitespace is ignored."""
    assert is_anagram("debit card", "bad credit") == True
    assert is_anagram("  race", "care  ") == True

def test_non_anagrams():
    """Test strings that are not anagrams."""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_empty_strings():
    """Test empty string scenarios."""
    assert is_anagram("", "") == True

def test_same_string():
    """Test a string with itself."""
    assert is_anagram("python", "python") == True

def test_type_error():
    """Verify type checking raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        is_anagram(123, "test")
    with pytest.raises(TypeError):
        is_anagram("test", None)
    with pytest.raises(TypeError):
        is_anagram([], "")
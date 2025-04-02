import pytest
from src.most_frequent_word import most_frequent_word

def test_basic_functionality():
    """Test finding the most frequent word in a simple text."""
    text = "the cat in the hat"
    assert most_frequent_word(text) == "the"

def test_multiple_words_same_frequency():
    """Test when multiple words have the same frequency."""
    text = "a b c a b c"
    result = most_frequent_word(text)
    assert result in ["a", "b", "c"]

def test_single_word():
    """Test with a single word."""
    text = "hello"
    assert most_frequent_word(text) == "hello"

def test_raised_on_empty_string():
    """Test that ValueError is raised for empty string."""
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        most_frequent_word("")

def test_raised_on_non_lowercase():
    """Test that ValueError is raised for non-lowercase text."""
    with pytest.raises(ValueError, match="Input text must contain only lowercase letters"):
        most_frequent_word("Hello WORLD")

def test_raised_on_whitespace_only():
    """Test that ValueError is raised for whitespace-only input."""
    with pytest.raises(ValueError, match="Input text must contain at least one word"):
        most_frequent_word("   ")
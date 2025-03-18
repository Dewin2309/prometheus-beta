import pytest
from src.string_utils import reverse_words

def test_basic_word_reversal():
    """Test basic word reversal"""
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_words():
    """Test reversal of multiple words"""
    assert reverse_words("One Two Three Four") == "Four Three Two One"

def test_preserve_spacing():
    """Test preservation of original spacing"""
    assert reverse_words("  Hello   World  ") == "  World   Hello  "

def test_with_numbers():
    """Test handling of words with numbers"""
    assert reverse_words("123 abc 456 def") == "def 456 abc 123"

def test_mixed_alphanumeric():
    """Test mixed alphanumeric words"""
    assert reverse_words("word1 word2 word3") == "word3 word2 word1"

def test_empty_string():
    """Test empty string input"""
    assert reverse_words("") == ""

def test_single_word():
    """Test single word input"""
    assert reverse_words("Hello") == "Hello"

def test_special_characters():
    """Test string with special characters"""
    assert reverse_words("hello! world@") == "world! hello@"

def test_whitespace_only():
    """Test string with only whitespace"""
    assert reverse_words("   ") == "   "
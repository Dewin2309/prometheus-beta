import pytest
from src.sentence_case import to_sentence_case

def test_basic_sentence_case():
    """Test basic sentence case conversion."""
    assert to_sentence_case("hello world") == "Hello world"
    assert to_sentence_case("PYTHON IS AWESOME") == "Python is awesome"

def test_already_sentence_case():
    """Test string that's already in sentence case."""
    assert to_sentence_case("Hello world") == "Hello world"

def test_single_word():
    """Test single word conversion."""
    assert to_sentence_case("HELLO") == "Hello"
    assert to_sentence_case("world") == "World"

def test_empty_string():
    """Test empty string handling."""
    assert to_sentence_case("") == ""

def test_whitespace_string():
    """Test string with only whitespace."""
    assert to_sentence_case(" ") == " "

def test_mixed_case():
    """Test mixed case conversion."""
    assert to_sentence_case("hElLo WoRlD") == "Hello world"

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_sentence_case(123)
    
    with pytest.raises(TypeError):
        to_sentence_case(None)

def test_special_characters():
    """Test conversion with special characters."""
    assert to_sentence_case("HELLO, WORLD!") == "Hello, world!"
    assert to_sentence_case("python-is-great") == "Python-is-great"
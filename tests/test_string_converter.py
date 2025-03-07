import pytest
from src.string_converter import to_camel_case

def test_basic_space_separated():
    """Test conversion of space-separated words."""
    assert to_camel_case("hello world") == "helloWorld"

def test_snake_case():
    """Test conversion of snake_case."""
    assert to_camel_case("hello_world") == "helloWorld"

def test_kebab_case():
    """Test conversion of kebab-case."""
    assert to_camel_case("hello-world") == "helloWorld"

def test_mixed_case_snake():
    """Test conversion of mixed case with snake_case."""
    assert to_camel_case("Hello_world") == "helloWorld"

def test_mixed_case_kebab():
    """Test conversion of mixed case with kebab-case."""
    assert to_camel_case("Hello-world") == "helloWorld"

def test_multiple_words():
    """Test conversion of multiple words."""
    assert to_camel_case("hello world python") == "helloWorldPython"

def test_empty_string():
    """Test conversion of empty string."""
    assert to_camel_case("") == ""

def test_single_word():
    """Test conversion of a single word."""
    assert to_camel_case("hello") == "hello"

def test_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_camel_case(123)

def test_whitespace_only():
    """Test conversion of whitespace-only string."""
    assert to_camel_case("   ") == ""

def test_mixed_separators():
    """Test conversion with mixed separators."""
    assert to_camel_case("hello_world-python test") == "helloWorldPythonTest"

def test_with_numbers():
    """Test conversion with numbers in the string."""
    assert to_camel_case("hello2_world3 test4") == "hello2World3Test4"
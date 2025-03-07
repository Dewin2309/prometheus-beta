import pytest
from src.string_converter import convert_to_alternating_case

def test_convert_to_alternating_case_normal_string():
    """Test conversion of a normal string."""
    assert convert_to_alternating_case("hello") == "hElLo"

def test_convert_to_alternating_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_single_char():
    """Test conversion of a single character."""
    assert convert_to_alternating_case("a") == "a"
    assert convert_to_alternating_case("B") == "b"

def test_convert_to_alternating_case_with_spaces():
    """Test conversion of a string with spaces."""
    assert convert_to_alternating_case("hello world") == "hElLo WoRlD"

def test_convert_to_alternating_case_with_special_chars():
    """Test conversion of a string with special characters."""
    assert convert_to_alternating_case("hello!world") == "hElLo!WoRlD"

def test_convert_to_alternating_case_invalid_input():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(None)
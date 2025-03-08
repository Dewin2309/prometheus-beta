import pytest
from src.string_utils import switch_cases

def test_switch_cases_basic():
    """Test basic case switching functionality"""
    assert switch_cases("AbC", "dEf") == "aBcDEF"

def test_switch_cases_all_lowercase():
    """Test switching cases for all lowercase input"""
    assert switch_cases("abc", "def") == "ABCdef"

def test_switch_cases_all_uppercase():
    """Test switching cases for all uppercase input"""
    assert switch_cases("ABC", "DEF") == "abcDEF"

def test_switch_cases_mixed_case():
    """Test switching cases for mixed case input"""
    assert switch_cases("HeLLo", "WoRLd") == "hEllOwoRlD"

def test_switch_cases_empty_strings():
    """Test behavior with empty strings"""
    assert switch_cases("", "") == ""

def test_switch_cases_non_string_input():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        switch_cases(123, "abc")
    with pytest.raises(TypeError):
        switch_cases("abc", [1, 2, 3])

def test_switch_cases_unequal_length():
    """Test error handling for strings of unequal length"""
    with pytest.raises(ValueError):
        switch_cases("abc", "abcd")

def test_switch_cases_special_characters():
    """Test handling of special characters and whitespace"""
    assert switch_cases("A1 b!", "c2 D?") == "a1 B!C2 d?"
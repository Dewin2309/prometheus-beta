import pytest
from src.even_numbers import extract_even_numbers

def test_extract_even_numbers_basic():
    """Test extracting even numbers from a simple sorted list."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert extract_even_numbers(input_list) == [2, 4, 6, 8, 10]

def test_extract_even_numbers_empty_list():
    """Test with an empty list."""
    assert extract_even_numbers([]) == []

def test_extract_even_numbers_no_evens():
    """Test with a list containing no even numbers."""
    assert extract_even_numbers([1, 3, 5, 7, 9]) == []

def test_extract_even_numbers_all_even():
    """Test with a list containing only even numbers."""
    assert extract_even_numbers([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]

def test_extract_even_numbers_negative_numbers():
    """Test with a list containing negative numbers."""
    input_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert extract_even_numbers(input_list) == [-4, -2, 0, 2, 4]

def test_input_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        extract_even_numbers("not a list")

def test_input_unsorted_error():
    """Test that ValueError is raised for unsorted list."""
    with pytest.raises(ValueError, match="Input must be a sorted list of unique integers"):
        extract_even_numbers([3, 1, 2, 4, 5])

def test_input_duplicate_error():
    """Test that ValueError is raised for list with duplicates."""
    with pytest.raises(ValueError, match="Input must be a sorted list of unique integers"):
        extract_even_numbers([1, 2, 2, 3, 4, 5])
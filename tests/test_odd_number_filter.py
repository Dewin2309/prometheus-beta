import pytest
from src.odd_number_filter import filter_odd_numbers

def test_filter_odd_numbers_basic():
    """Test filtering odd numbers from a mixed list of integers."""
    assert filter_odd_numbers([1, 2, 3, 4, 5, 6, 7]) == [1, 3, 5, 7]

def test_filter_odd_numbers_empty_list():
    """Test filtering an empty list."""
    assert filter_odd_numbers([]) == []

def test_filter_odd_numbers_no_odds():
    """Test list with no odd numbers."""
    assert filter_odd_numbers([2, 4, 6, 8]) == []

def test_filter_odd_numbers_only_odds():
    """Test list with only odd numbers."""
    assert filter_odd_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_filter_odd_numbers_negative_odds():
    """Test filtering with negative odd numbers."""
    assert filter_odd_numbers([-1, -2, -3, 0, 1, 2, 3]) == [-1, -3, 1, 3]

def test_filter_odd_numbers_type_error_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_numbers("not a list")

def test_filter_odd_numbers_type_error_non_numeric():
    """Test raising TypeError for list with non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        filter_odd_numbers([1, 2, "three", 4])

def test_filter_odd_numbers_floats():
    """Test handling of float values (only integers should be considered)."""
    assert filter_odd_numbers([1.5, 2, 3.0, 4, 5]) == []
    assert filter_odd_numbers([5]) == [5]  # Integer 5 should be included
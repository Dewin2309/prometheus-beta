import pytest
from src.integer_list_sum import sum_integers

def test_sum_empty_list():
    """Test summing an empty list returns 0."""
    assert sum_integers([]) == 0

def test_sum_single_element():
    """Test summing a list with a single element."""
    assert sum_integers([42]) == 42

def test_sum_multiple_positive_integers():
    """Test summing multiple positive integers."""
    assert sum_integers([1, 2, 3, 4, 5]) == 15

def test_sum_with_negative_integers():
    """Test summing list with negative and positive integers."""
    assert sum_integers([-1, 0, 1]) == 0

def test_large_numbers():
    """Test summing large integers."""
    assert sum_integers([1000000, 2000000, -500000]) == 2500000

def test_invalid_input_not_list():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integers(42)

def test_invalid_input_non_integers():
    """Test that list with non-integer elements raises TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1, 2, '3', 4])

def test_mixed_positive_and_negative():
    """Test summing a list with mixed positive and negative integers."""
    assert sum_integers([-10, 5, 15, -5]) == 5
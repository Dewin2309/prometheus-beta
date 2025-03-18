import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4]) == 10

def test_all_negative_numbers():
    """Test with an array of all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element array."""
    assert max_subarray_sum([42]) == 42

def test_zeros_and_negative_numbers():
    """Test with an array containing zeros and negative numbers."""
    assert max_subarray_sum([0, -1, 0, -2]) == 0

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_invalid_input_not_a_list():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
        max_subarray_sum(123)
        max_subarray_sum(None)
import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with an array of mixed positive and negative numbers."""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with an array of all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element array."""
    assert max_subarray_sum([5]) == 5

def test_zero_elements():
    """Test input type validation."""
    with pytest.raises(TypeError):
        max_subarray_sum(0)

def test_empty_list():
    """Test empty list input."""
    with pytest.raises(ValueError):
        max_subarray_sum([])

def test_large_numbers():
    """Test with large numbers."""
    assert max_subarray_sum([1000000, -500000, 600000]) == 1100000

def test_alternating_signs():
    """Test with alternating positive and negative numbers."""
    assert max_subarray_sum([1, -1, 2, -2, 3, -3]) == 3

def test_zeros():
    """Test with array containing zeros."""
    assert max_subarray_sum([0, 0, 0, 1, 0]) == 1

def test_subarray_at_start():
    """Test when max subarray is at the start of the list."""
    assert max_subarray_sum([5, 4, -10, 1]) == 9

def test_subarray_at_end():
    """Test when max subarray is at the end of the list."""
    assert max_subarray_sum([-10, 1, 5, 4]) == 10
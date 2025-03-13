import pytest
from src.local_max_finder import find_local_maxima

def test_basic_local_maxima():
    """Test finding local maxima in a typical array"""
    assert find_local_maxima([1, 3, 2, 4, 1, 5]) == [1, 3, 5]

def test_ascending_array():
    """Test an ascending array should return last index"""
    assert find_local_maxima([1, 2, 3, 4, 5]) == [4]

def test_descending_array():
    """Test a descending array should return first index"""
    assert find_local_maxima([5, 4, 3, 2, 1]) == [0]

def test_single_element_array():
    """Test an array with a single element"""
    assert find_local_maxima([42]) == [0]

def test_two_element_array_first_max():
    """Test a two-element array where the first is larger"""
    assert find_local_maxima([5, 3]) == [0]

def test_two_element_array_second_max():
    """Test a two-element array where the second is larger"""
    assert find_local_maxima([3, 5]) == [1]

def test_multiple_local_maxima():
    """Test an array with multiple local maxima"""
    assert find_local_maxima([1, 5, 3, 7, 2, 8, 4]) == [1, 3, 5]

def test_all_equal_elements():
    """Test an array with all equal elements"""
    assert find_local_maxima([2, 2, 2, 2, 2]) == []

def test_invalid_input_type():
    """Test that non-list inputs raise TypeError"""
    with pytest.raises(TypeError):
        find_local_maxima("not a list")

def test_empty_input():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError):
        find_local_maxima([])
import pytest
from src.first_occurrence_binary_search import find_first_occurrence

def test_find_first_occurrence_basic():
    """Test basic functionality of finding first occurrence"""
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    assert find_first_occurrence(arr, 3) == 3

def test_find_first_occurrence_first_element():
    """Test finding first element in the array"""
    arr = [1, 1, 2, 3, 4, 5]
    assert find_first_occurrence(arr, 1) == 0

def test_find_first_occurrence_last_element():
    """Test finding last element in the array"""
    arr = [1, 2, 3, 4, 5, 5]
    assert find_first_occurrence(arr, 5) == 4

def test_find_first_occurrence_not_found():
    """Test when target is not in the array"""
    arr = [1, 2, 3, 4, 5]
    assert find_first_occurrence(arr, 6) == -1

def test_find_first_occurrence_empty_array():
    """Test with an empty array"""
    arr = []
    assert find_first_occurrence(arr, 1) == -1

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_first_occurrence("not a list", 1)

def test_invalid_input_non_integer_target():
    """Test raising TypeError for non-integer target"""
    with pytest.raises(TypeError, match="Target must be an integer"):
        find_first_occurrence([1, 2, 3], "target")

def test_invalid_input_non_positive_integers():
    """Test raising ValueError for non-positive integers"""
    with pytest.raises(ValueError, match="Array must contain only positive integers"):
        find_first_occurrence([1, 2, -3, 4], 3)
        
def test_single_element_array_found():
    """Test single element array when target is found"""
    arr = [5]
    assert find_first_occurrence(arr, 5) == 0

def test_single_element_array_not_found():
    """Test single element array when target is not found"""
    arr = [5]
    assert find_first_occurrence(arr, 6) == -1
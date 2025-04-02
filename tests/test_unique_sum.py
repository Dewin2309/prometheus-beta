import pytest
from src.unique_sum import sum_unique_elements

def test_sum_unique_elements_basic():
    """Test basic functionality with a mix of unique and duplicate elements"""
    assert sum_unique_elements([1, 2, 3, 2]) == 4  # 1 + 3
    assert sum_unique_elements([1, 1, 1, 1]) == 0  # No unique elements
    assert sum_unique_elements([5, 5, 7, 7, 8]) == 8  # Only one unique element

def test_sum_unique_elements_empty_list():
    """Test with an empty list"""
    assert sum_unique_elements([]) == 0

def test_sum_unique_elements_all_unique():
    """Test with all unique elements"""
    assert sum_unique_elements([1, 2, 3, 4, 5]) == 15

def test_sum_unique_elements_negative_numbers():
    """Test with negative numbers"""
    assert sum_unique_elements([-1, -1, 2, 3, 2]) == 2  # 3 is unique

def test_sum_unique_elements_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_unique_elements(123)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1, 2, 'a', 3])

def test_sum_unique_elements_zero():
    """Test with zero values"""
    assert sum_unique_elements([0, 0, 1, 1]) == 0  # No unique elements
    assert sum_unique_elements([0, 1, 2]) == 3  # 0, 1, and 2 are unique
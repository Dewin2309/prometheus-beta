import pytest
from src.list_operations import calculate_sum

def test_normal_case():
    """Test with a standard list of integers."""
    assert calculate_sum([1, 2, 3, 4, 5]) == 40
    # Explanation: (1*0) + (2*1) + (3*2) + (4*3) + (5*4) = 0 + 2 + 6 + 12 + 20 = 40

def test_empty_list():
    """Test with an empty list."""
    assert calculate_sum([]) == 0

def test_single_element_list():
    """Test with a single-element list."""
    assert calculate_sum([5]) == 0

def test_negative_numbers():
    """Test with negative numbers."""
    assert calculate_sum([-1, -2, -3]) == -8
    # Explanation: (-1*0) + (-2*1) + (-3*2) = 0 - 2 - 6 = -8

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_invalid_input_non_integers():
    """Test raising TypeError for list with non-integer elements."""
    with pytest.raises(TypeError, match="List must contain only integers"):
        calculate_sum([1, 2, "3", 4])
        
def test_zero_list():
    """Test with a list of zeros."""
    assert calculate_sum([0, 0, 0]) == 0
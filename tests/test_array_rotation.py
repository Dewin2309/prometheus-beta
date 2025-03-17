import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    """Test basic array rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation equal to array length"""
    assert rotate_array([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_partial_rotation():
    """Test rotation less than array length"""
    assert rotate_array([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array([], 3) == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    assert rotate_array([1], 5) == [1]

def test_rotation_greater_than_length():
    """Test rotation amount greater than array length"""
    assert rotate_array([1, 2, 3], 7) == [3, 1, 2]

def test_zero_rotation():
    """Test zero rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

def test_negative_rotation_raises_error():
    """Test that negative rotation raises a ValueError"""
    with pytest.raises(ValueError):
        rotate_array([1, 2, 3], -1)

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError):
        rotate_array("not a list", 2)

def test_non_integer_rotation_raises_error():
    """Test that non-integer rotation amount raises a TypeError"""
    with pytest.raises(TypeError):
        rotate_array([1, 2, 3], "2")
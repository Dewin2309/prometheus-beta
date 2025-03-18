import pytest
from src.library_sort import library_sort

def test_library_sort_basic():
    """Test basic sorting of integers"""
    assert library_sort([5, 2, 9, 1, 7, 6]) == [1, 2, 5, 6, 7, 9]

def test_library_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert library_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_library_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    assert library_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_library_sort_duplicate_values():
    """Test sorting with duplicate values"""
    assert library_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_library_sort_empty_list():
    """Test sorting an empty list"""
    assert library_sort([]) == []

def test_library_sort_single_element():
    """Test sorting a single-element list"""
    assert library_sort([42]) == [42]

def test_library_sort_strings():
    """Test sorting strings"""
    assert library_sort(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]

def test_library_sort_mixed_types():
    """Test sorting mixed numeric types"""
    result = library_sort([5, 2.5, 7, 1, 3.14])
    assert result == [1, 2.5, 3.14, 5, 7]

def test_library_sort_invalid_input():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        library_sort("not a list")
        library_sort(123)
        library_sort(None)
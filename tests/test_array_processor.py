import pytest
from src.array_processor import process_multidim_array

def test_process_multidim_array_basic():
    # Basic test with mixed arrays
    input_arr = [[1, 2], [3, 4], [5, 6]]
    expected = [6, 5, 4, 3, 2, 1]
    assert process_multidim_array(input_arr) == expected

def test_process_multidim_array_with_empty_subarrays():
    # Test with empty sub-arrays
    input_arr = [[1, 2], [], [3, 4], []]
    expected = [4, 3, 2, 1]
    assert process_multidim_array(input_arr) == expected

def test_process_multidim_array_with_duplicates():
    # Test removing duplicates while maintaining order
    input_arr = [[1, 2, 2], [3, 1], [4, 3]]
    expected = [2, 1, 3, 4]
    result = process_multidim_array(input_arr)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_process_multidim_array_empty_input():
    # Test with empty input
    input_arr = []
    expected = []
    assert process_multidim_array(input_arr) == expected

def test_process_multidim_array_nested():
    # Test with more complex nested structure
    input_arr = [[1, 2], [3, [4, 5]], [], [6, 7]]
    expected = [7, 6, 5, 4, 3, 2, 1]
    result = process_multidim_array(input_arr)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_process_multidim_array_different_types():
    # Test with different types of elements
    input_arr = [['a', 'b'], [1, 2], ['b', 'c']]
    expected = ['b', 'a', 2, 1, 'c']
    result = process_multidim_array(input_arr)
    assert result == expected, f"Expected {expected}, but got {result}"
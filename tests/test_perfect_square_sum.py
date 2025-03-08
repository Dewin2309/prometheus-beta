import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from perfect_square_sum import sum_perfect_squares_from_set

def test_basic_perfect_squares():
    """Test basic set of perfect squares"""
    test_set = {1, 4, 9, 16}
    assert sum_perfect_squares_from_set(test_set) == 30

def test_mixed_numbers():
    """Test a set with mixed numbers that can form perfect squares"""
    test_set = {2, 3, 4, 5, 6}
    assert sum_perfect_squares_from_set(test_set) == 25  # 1 + 4 + 16 + 4

def test_no_perfect_squares():
    """Test a set with no perfect squares"""
    test_set = {2, 3, 5, 7}
    assert sum_perfect_squares_from_set(test_set) == 0

def test_negative_numbers():
    """Test set with negative numbers"""
    test_set = {-1, -4, 2, 3}
    assert sum_perfect_squares_from_set(test_set) == 4

def test_large_set():
    """Test a larger set with multiple perfect squares"""
    test_set = {10, 20, 30, 40, 50, 2, 3}
    assert sum_perfect_squares_from_set(test_set) == 1156  # 4 + 16 + 1024 + 100 + 16

def test_invalid_input_not_set():
    """Test that a non-set input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a set"):
        sum_perfect_squares_from_set([1, 2, 3])

def test_invalid_input_non_integers():
    """Test that a set with non-integer elements raises TypeError"""
    with pytest.raises(TypeError, match="All elements in the set must be integers"):
        sum_perfect_squares_from_set({1, 2, "3", 4.5})

def test_empty_set():
    """Test an empty set"""
    assert sum_perfect_squares_from_set(set()) == 0
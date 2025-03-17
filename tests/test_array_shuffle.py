import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_basic_list():
    """Test shuffling a basic list of integers."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that shuffled list has same elements
    assert set(shuffled) == set(original)
    
    # Check that it's not the same as original (with some probabilistic approach)
    assert shuffled != original

def test_shuffle_empty_list():
    """Test shuffling an empty list."""
    assert shuffle_array([]) == []

def test_shuffle_single_element_list():
    """Test shuffling a list with a single element."""
    single_list = [42]
    assert shuffle_array(single_list) == single_list

def test_shuffle_list_with_duplicates():
    """Test shuffling a list with duplicate elements."""
    original = [1, 2, 2, 3, 3, 3]
    shuffled = shuffle_array(original)
    
    # Check that shuffled list has same elements
    assert sorted(shuffled) == sorted(original)
    
    # Check that it's not the same as original (with some probabilistic approach)
    assert shuffled != original

def test_shuffle_different_types():
    """Test shuffling a list with different types of elements."""
    original = [1, 'a', True, 3.14, None]
    shuffled = shuffle_array(original)
    
    # Check that shuffled list has same elements
    assert set(shuffled) == set(original)
    
    # Check that it's not the same as original (with some probabilistic approach)
    assert shuffled != original

def test_shuffle_raises_type_error():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(123)

def test_shuffle_randomness():
    """Test that the shuffle function provides randomness.
    
    This test checks if multiple shuffles are likely to produce different orders.
    Due to the probabilistic nature, we use multiple attempts.
    """
    original = list(range(10))
    different_order_count = 0
    num_attempts = 50
    
    for _ in range(num_attempts):
        shuffled = shuffle_array(original)
        if shuffled != original:
            different_order_count += 1
    
    # We expect most shuffles to be different from the original
    assert different_order_count > num_attempts * 0.9
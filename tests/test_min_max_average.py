import pytest
from src.min_max_average import calculate_min_max_average

def test_standard_case():
    """Test with a standard set of numbers."""
    numbers = [1, 2, 3, 4, 5, 6]
    assert calculate_min_max_average(numbers) == 3.5

def test_unsorted_numbers():
    """Test with unsorted input numbers."""
    numbers = [6, 1, 4, 2, 5, 3]
    assert calculate_min_max_average(numbers) == 3.5

def test_negative_numbers():
    """Test with negative numbers."""
    numbers = [-1, -2, -3, 4, 5, 6]
    assert calculate_min_max_average(numbers) == 2.5

def test_floating_point_numbers():
    """Test with floating point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    assert calculate_min_max_average(numbers) == 4.5

def test_input_length_error():
    """Test error handling for incorrect number of inputs."""
    with pytest.raises(ValueError, match="Input must contain exactly six numbers"):
        calculate_min_max_average([1, 2, 3, 4, 5])

def test_input_length_too_many():
    """Test error handling for too many inputs."""
    with pytest.raises(ValueError, match="Input must contain exactly six numbers"):
        calculate_min_max_average([1, 2, 3, 4, 5, 6, 7])
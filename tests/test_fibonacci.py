import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test the base cases for Fibonacci sequence."""
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1

def test_fibonacci_sequence():
    """Test several known Fibonacci numbers."""
    assert fibonacci(3) == 2  # 1 + 1
    assert fibonacci(4) == 3  # 1 + 2
    assert fibonacci(5) == 5  # 2 + 3
    assert fibonacci(6) == 8  # 3 + 5
    assert fibonacci(7) == 13  # 5 + 8

def test_fibonacci_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci(-1)

def test_fibonacci_type_error():
    """Test type checking for invalid input types."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(1.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("3")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(None)
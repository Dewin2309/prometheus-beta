import pytest
import math

from src.fibonacci import extended_fibonacci

def test_positive_integers():
    """Test Fibonacci sequence for positive integer indices"""
    assert extended_fibonacci(0) == 0
    assert extended_fibonacci(1) == 1
    assert extended_fibonacci(2) == 1
    assert extended_fibonacci(3) == 2
    assert extended_fibonacci(4) == 3
    assert extended_fibonacci(5) == 5
    assert extended_fibonacci(6) == 8

def test_negative_integers():
    """Test Fibonacci sequence for negative integer indices"""
    assert extended_fibonacci(-1) == 1
    assert extended_fibonacci(-2) == -1
    assert extended_fibonacci(-3) == 2
    assert extended_fibonacci(-4) == -3
    assert extended_fibonacci(-5) == 5

def test_float_inputs():
    """Test Fibonacci-like interpolation for float inputs"""
    # Check that fractional inputs interpolate between integer Fibonacci numbers
    assert math.isclose(extended_fibonacci(0.5), 0.5, rel_tol=1e-9)
    assert math.isclose(extended_fibonacci(1.5), 1.5, rel_tol=1e-9)
    assert math.isclose(extended_fibonacci(2.25), 1.625, rel_tol=1e-9)

def test_float_negative_inputs():
    """Test Fibonacci-like interpolation for negative float inputs"""
    assert math.isclose(extended_fibonacci(-0.5), 0.5, rel_tol=1e-9)
    assert math.isclose(extended_fibonacci(-1.5), -0.5, rel_tol=1e-9)

def test_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        extended_fibonacci("not a number")
    with pytest.raises(TypeError):
        extended_fibonacci(None)
    with pytest.raises(TypeError):
        extended_fibonacci([1, 2, 3])

def test_large_indices():
    """Test larger indices to ensure computational stability"""
    # Verify some larger index calculations
    assert extended_fibonacci(10) == 55
    assert extended_fibonacci(-10) == 55
    assert extended_fibonacci(20) == 6765

def test_zero_input():
    """Explicitly test zero input"""
    assert extended_fibonacci(0) == 0
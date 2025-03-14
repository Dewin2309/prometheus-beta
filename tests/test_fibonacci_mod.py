import pytest
from src.fibonacci_mod import generate_modified_fibonacci

def test_generate_modified_fibonacci_zero():
    """Test sequence for n = 0"""
    assert generate_modified_fibonacci(0) == []

def test_generate_modified_fibonacci_one():
    """Test sequence for n = 1"""
    assert generate_modified_fibonacci(1) == [1]

def test_generate_modified_fibonacci_two():
    """Test sequence for n = 2"""
    assert generate_modified_fibonacci(2) == [1, 1]

def test_generate_modified_fibonacci_small_numbers():
    """Test sequence for small numbers"""
    result = generate_modified_fibonacci(10)
    assert result == [1, 1, 3]

def test_generate_modified_fibonacci_larger_numbers():
    """Test sequence for larger numbers"""
    result = generate_modified_fibonacci(20)
    assert result == [1, 1, 3, 9]

def test_divisibility_condition():
    """Verify divisibility condition for the sequence"""
    result = generate_modified_fibonacci(50)
    for i in range(2, len(result)):
        assert (result[i-2] + result[i-1]) % 3 == 0, \
            f"Divisibility condition not met for numbers {result[i-2]}, {result[i-1]}"

def test_negative_input():
    """Test that negative input raises ValueError"""
    with pytest.raises(ValueError):
        generate_modified_fibonacci(-1)

def test_sequence_does_not_exceed_limit():
    """Verify that no number in the sequence exceeds the input limit"""
    limit = 15
    result = generate_modified_fibonacci(limit)
    assert all(num <= limit for num in result), \
        f"Sequence contains numbers larger than {limit}"
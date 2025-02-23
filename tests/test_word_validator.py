import pytest
from src.word_validator import Queue, is_word_valid

def test_queue_basic_operations():
    """Test basic Queue operations."""
    q = Queue()
    assert q.is_empty() == True
    
    q.enqueue(1)
    assert q.is_empty() == False
    
    item = q.dequeue()
    assert item == 1
    assert q.is_empty() == True

def test_queue_multiple_operations():
    """Test multiple Queue operations."""
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    assert q.dequeue() == 10
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.is_empty() == True

def test_queue_empty_dequeue():
    """Test dequeuing from an empty queue raises an exception."""
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()

def test_word_validation_basic():
    """Test basic word validation."""
    rules = {
        'min_length': 3,
        'max_length': 10
    }
    
    assert is_word_valid('hello', rules) == True
    assert is_word_valid('hi', rules) == False
    assert is_word_valid('verylongword', rules) == False

def test_word_validation_allowed_chars():
    """Test validation with allowed characters."""
    rules = {
        'allowed_chars': 'abcdefg'
    }
    
    assert is_word_valid('abc', rules) == True
    assert is_word_valid('abcdefg', rules) == True
    assert is_word_valid('abcd', rules) == False
    
def test_word_validation_prohibited_chars():
    """Test validation with prohibited characters."""
    rules = {
        'prohibited_chars': ['1', '2', '3']
    }
    
    assert is_word_valid('hello', rules) == True
    assert is_word_valid('hello1', rules) == False

def test_word_validation_start_end_chars():
    """Test validation with start and end character rules."""
    rules = {
        'start_chars': ['a', 'b'],
        'end_chars': ['x', 'y']
    }
    
    assert is_word_valid('abcdx', rules) == True
    assert is_word_valid('cdefg', rules) == False
    assert is_word_valid('abcde', rules) == False

def test_word_validation_custom_function():
    """Test validation with a custom validation function."""
    def is_palindrome(word):
        return word == word[::-1]
    
    rules = {
        'custom_validation': is_palindrome
    }
    
    assert is_word_valid('racecar', rules) == True
    assert is_word_valid('hello', rules) == False

def test_word_validation_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(ValueError):
        is_word_valid('hello', 'not a dict')
    
    assert is_word_valid(123, {}) == False
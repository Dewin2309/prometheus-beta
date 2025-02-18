import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_basic():
    """Test basic Burrows-Wheeler Transform functionality"""
    text = "banana"
    transformed_text, original_index = burrows_wheeler_transform(text)
    assert isinstance(transformed_text, str)
    assert isinstance(original_index, int)

def test_burrows_wheeler_roundtrip():
    """Test that BWT and inverse BWT recover the original text"""
    test_cases = [
        "banana",
        "mississippi",
        "hello world",
        "abracadabra",
        ""
    ]
    
    for text in test_cases:
        # Perform Burrows-Wheeler Transform
        transformed_text, original_index = burrows_wheeler_transform(text)
        
        # Reverse the transform
        recovered_text = inverse_burrows_wheeler_transform(transformed_text, original_index)
        
        assert recovered_text == text, f"Failed for input: {text}"

def test_edge_cases():
    """Test edge cases like empty string, single character, special characters"""
    # Empty string
    assert burrows_wheeler_transform("") == ('', 0)
    assert inverse_burrows_wheeler_transform("", 0) == ""
    
    # Single character
    single_char = "a"
    transformed, index = burrows_wheeler_transform(single_char)
    assert inverse_burrows_wheeler_transform(transformed, index) == single_char

def test_transform_properties():
    """Verify specific properties of Burrows-Wheeler Transform"""
    text = "banana"
    transformed_text, original_index = burrows_wheeler_transform(text)
    
    # Check that transformed text has same length as original
    assert len(transformed_text) == len(text) + 1
    
    # Verify index is within valid range
    assert 0 <= original_index < len(transformed_text)

def test_error_handling():
    """Verify error handling for invalid inputs"""
    # Test with non-string input would raise TypeError
    with pytest.raises(TypeError):
        burrows_wheeler_transform(12345)
    
    with pytest.raises(TypeError):
        inverse_burrows_wheeler_transform(12345, 0)
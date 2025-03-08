import pytest
from src.roman_numerals import convert_to_roman

def test_convert_to_roman_basic_cases():
    """Test basic Roman numeral conversions"""
    assert convert_to_roman(1) == 'I'
    assert convert_to_roman(4) == 'IV'
    assert convert_to_roman(9) == 'IX'
    assert convert_to_roman(49) == 'XLIX'
    assert convert_to_roman(99) == 'XCIX'
    assert convert_to_roman(500) == 'D'
    assert convert_to_roman(2023) == 'MMXXIII'
    assert convert_to_roman(3999) == 'MMMCMXCIX'

def test_convert_to_roman_zero():
    """Test conversion of 0"""
    assert convert_to_roman(0) == ''

def test_convert_to_roman_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        convert_to_roman(-1)
    
    # Test numbers above maximum
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        convert_to_roman(4000)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        convert_to_roman(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        convert_to_roman("123")

def test_convert_to_roman_edge_cases():
    """Test edge cases and specific Roman numeral rules"""
    # Test all special subtractive notation cases
    assert convert_to_roman(4) == 'IV'    # 4 as IV
    assert convert_to_roman(9) == 'IX'    # 9 as IX
    assert convert_to_roman(40) == 'XL'   # 40 as XL
    assert convert_to_roman(90) == 'XC'   # 90 as XC
    assert convert_to_roman(400) == 'CD'  # 400 as CD
    assert convert_to_roman(900) == 'CM'  # 900 as CM
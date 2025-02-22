import pytest
import sys
sys.path.append('src')

from lzma2_compression import lzma2_compress, lzma2_decompress

def test_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, this is a test string for LZMA2 compression!"
    compressed_data = lzma2_compress(original_data)
    
    # Compressed data should be different from original
    assert compressed_data != original_data
    assert len(compressed_data) < len(original_data)
    
    # Decompress and verify
    decompressed_data = lzma2_decompress(compressed_data)
    assert decompressed_data == original_data

def test_string_input():
    """Test compression with string input"""
    original_data = "Hello, world! Testing string compression."
    compressed_data = lzma2_compress(original_data)
    decompressed_data = lzma2_decompress(compressed_data)
    
    assert decompressed_data.decode('utf-8') == original_data

def test_different_compression_levels():
    """Test compression with different levels"""
    data = b"Test data for checking different compression levels"
    
    # Try different compression levels
    for level in range(10):
        compressed = lzma2_compress(data, compression_level=level)
        decompressed = lzma2_decompress(compressed)
        assert decompressed == data

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        lzma2_compress(123)
    
    with pytest.raises(TypeError):
        lzma2_decompress("Not bytes")

def test_invalid_compression_level():
    """Test error handling for invalid compression level"""
    with pytest.raises(ValueError):
        lzma2_compress(b"test", compression_level=10)
    
    with pytest.raises(ValueError):
        lzma2_compress(b"test", compression_level=-1)
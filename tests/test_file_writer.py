import os
import pytest
import tempfile

from src.file_writer import write_string_to_file

def test_write_string_to_file_basic():
    """Test basic string writing to a file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'test.txt')
        test_content = "Hello, world!"
        
        result = write_string_to_file(test_file, test_content)
        assert result is True
        
        with open(test_file, 'r') as f:
            assert f.read() == test_content

def test_write_string_to_file_nested_directory():
    """Test writing to a file in a nested directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'nested', 'dir', 'test.txt')
        test_content = "Nested directory test"
        
        result = write_string_to_file(test_file, test_content)
        assert result is True
        
        with open(test_file, 'r') as f:
            assert f.read() == test_content

def test_write_string_to_file_append():
    """Test appending to an existing file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'append.txt')
        
        # First write
        write_string_to_file(test_file, "First line\n")
        
        # Append
        write_string_to_file(test_file, "Second line\n", mode='a')
        
        with open(test_file, 'r') as f:
            assert f.read() == "First line\n" + "Second line\n"

def test_write_string_to_file_non_utf8_encoding():
    """Test writing with a different encoding."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'encoding.txt')
        test_content = "Héllo, wörld!"
        
        result = write_string_to_file(test_file, test_content, encoding='latin-1')
        assert result is True
        
        with open(test_file, 'r', encoding='latin-1') as f:
            assert f.read() == test_content

def test_write_string_to_file_invalid_input_types():
    """Test error handling for invalid input types."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'test.txt')
        
        with pytest.raises(TypeError, match="file_path must be a string"):
            write_string_to_file(123, "test")
        
        with pytest.raises(TypeError, match="content must be a string"):
            write_string_to_file(test_file, 123)

def test_write_string_to_file_empty_path():
    """Test error handling for empty file path."""
    with pytest.raises(ValueError, match="file_path cannot be empty"):
        write_string_to_file("", "test")
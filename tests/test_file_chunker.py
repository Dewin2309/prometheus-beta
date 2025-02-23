import os
import pytest
import tempfile
import shutil
from src.file_chunker import split_file_into_chunks, _parse_size_string

@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def create_test_file(temp_dir, size=5 * 1024):
    """Create a test file with random content."""
    test_file = os.path.join(temp_dir, 'test_input.txt')
    with open(test_file, 'wb') as f:
        f.write(os.urandom(size))
    return test_file

def test_split_file_basic(temp_dir):
    """Test basic file splitting functionality."""
    input_file = create_test_file(temp_dir)
    chunk_files = split_file_into_chunks(input_file, chunk_size=1024, output_dir=temp_dir)
    
    assert len(chunk_files) > 1
    for chunk_file in chunk_files:
        assert os.path.exists(chunk_file)
        assert os.path.getsize(chunk_file) <= 1024

def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        split_file_into_chunks('/path/to/nonexistent/file.txt')

def test_invalid_chunk_size(temp_dir):
    """Test handling of invalid chunk sizes."""
    input_file = create_test_file(temp_dir)
    
    with pytest.raises(ValueError):
        split_file_into_chunks(input_file, chunk_size=0)
    
    with pytest.raises(ValueError):
        split_file_into_chunks(input_file, chunk_size=-100)

def test_size_parsing():
    """Test size string parsing."""
    assert _parse_size_string('1KB') == 1024
    assert _parse_size_string('1MB') == 1024 * 1024
    assert _parse_size_string('1GB') == 1024 * 1024 * 1024
    assert _parse_size_string('10MB') == 10 * 1024 * 1024

def test_size_parsing_invalid():
    """Test invalid size string parsing."""
    with pytest.raises(ValueError):
        _parse_size_string('invalid')
    
    with pytest.raises(ValueError):
        _parse_size_string('10XB')

def test_default_output_dir(temp_dir):
    """Test default output directory behavior."""
    input_file = create_test_file(temp_dir)
    chunk_files = split_file_into_chunks(input_file, chunk_size=1024)
    
    # Chunks should be in same directory as input file
    for chunk_file in chunk_files:
        assert os.path.dirname(chunk_file) == temp_dir

def test_chunk_filename_pattern(temp_dir):
    """Test chunk filename pattern."""
    input_file = create_test_file(temp_dir)
    chunk_files = split_file_into_chunks(input_file, chunk_size=1024)
    
    for chunk_file in chunk_files:
        assert '.part' in os.path.basename(chunk_file)
        
def test_zero_byte_file(temp_dir):
    """Test splitting a zero-byte file."""
    input_file = os.path.join(temp_dir, 'empty.txt')
    with open(input_file, 'w') as f:
        pass
    
    chunk_files = split_file_into_chunks(input_file, chunk_size=1024)
    assert len(chunk_files) == 0  # No chunks created
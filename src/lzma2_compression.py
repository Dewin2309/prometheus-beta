import lzma
import io

def lzma2_compress(input_data, compression_level=6):
    """
    Compress input data using LZMA2 compression algorithm.
    
    Args:
        input_data (bytes or str): Data to be compressed
        compression_level (int, optional): Compression level (0-9). Defaults to 6.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If compression level is out of range
    """
    # Validate input type
    if not isinstance(input_data, (bytes, str)):
        raise TypeError("Input must be bytes or str")
    
    # Convert string to bytes if needed
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Use LZMA to compress the data
    compressor = lzma.LZMA(preset=compression_level)
    compressed_data = compressor.compress(input_data) + compressor.flush()
    
    return compressed_data

def lzma2_decompress(compressed_data):
    """
    Decompress data compressed with LZMA2 algorithm.
    
    Args:
        compressed_data (bytes): Data to be decompressed
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        lzma.LZMAError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Use LZMA to decompress the data
    decompressor = lzma.LZMA()
    decompressed_data = decompressor.decompress(compressed_data)
    
    return decompressed_data
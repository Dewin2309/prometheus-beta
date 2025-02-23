import os
from typing import Union, Optional

def split_file_into_chunks(
    input_file: str, 
    chunk_size: Union[int, str] = 1024 * 1024,  # Default 1 MB
    output_dir: Optional[str] = None
) -> list:
    """
    Split a large file into smaller chunks.

    Args:
        input_file (str): Path to the input file to be split
        chunk_size (int or str): Size of each chunk in bytes. 
            Can be an integer or string with units like 'KB', 'MB', 'GB'
        output_dir (str, optional): Directory to save chunks. 
            If None, uses the same directory as input file

    Returns:
        list: List of paths to the created chunk files

    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If chunk_size is invalid
        PermissionError: If there are permission issues
    """
    # Validate input file
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")

    # Convert chunk_size if it's a string with units
    if isinstance(chunk_size, str):
        chunk_size = _parse_size_string(chunk_size)

    # Validate chunk size
    if not isinstance(chunk_size, int) or chunk_size <= 0:
        raise ValueError(f"Invalid chunk size: {chunk_size}. Must be a positive integer")

    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(input_file) or '.'
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Prepare chunk file paths
    base_filename = os.path.basename(input_file)
    chunk_files = []

    try:
        with open(input_file, 'rb') as f:
            chunk_number = 1
            while True:
                # Read chunk
                chunk = f.read(chunk_size)
                
                # Break if no more data
                if not chunk:
                    break

                # Create chunk filename
                chunk_filename = os.path.join(
                    output_dir, 
                    f"{base_filename}.part{chunk_number:03d}"
                )

                # Write chunk
                with open(chunk_filename, 'wb') as chunk_file:
                    chunk_file.write(chunk)
                
                chunk_files.append(chunk_filename)
                chunk_number += 1

    except PermissionError:
        raise PermissionError(f"Permission denied when writing chunks for {input_file}")
    except IOError as e:
        raise IOError(f"Error processing file: {e}")

    return chunk_files

def _parse_size_string(size_str: str) -> int:
    """
    Parse size string with units to bytes.
    
    Supports 'B', 'KB', 'MB', 'GB' units (case-insensitive)
    
    Args:
        size_str (str): Size string like '10MB'
    
    Returns:
        int: Size in bytes
    
    Raises:
        ValueError: If size string is invalid
    """
    size_str = size_str.upper().strip()
    
    # Map of unit multipliers
    multipliers = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 * 1024,
        'GB': 1024 * 1024 * 1024
    }
    
    # Try to parse size
    for unit, multiplier in multipliers.items():
        if size_str.endswith(unit):
            try:
                # First, remove the unit
                value_str = size_str[:-len(unit)].strip()
                
                # Use 1 if no value specified (e.g., 'KB' -> 1)
                value = float(value_str) if value_str else 1.0
                
                return int(value * multiplier)
            except ValueError:
                break
    
    # Direct parsing if no unit is provided
    try:
        return int(size_str)
    except ValueError:
        pass
    
    # Special case: if first part matches a known multiplier with no number
    for unit in multipliers.keys():
        if size_str == unit:
            return multipliers[unit]
    
    raise ValueError(f"Invalid size format: {size_str}. Use format like '10MB', '1KB', or '1024'")
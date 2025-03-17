import os

def write_string_to_file(file_path, content, encoding='utf-8', mode='w'):
    """
    Write a string to a text file with configurable parameters.

    Args:
        file_path (str): The path to the file where the string will be written.
        content (str): The string content to write to the file.
        encoding (str, optional): The file encoding. Defaults to 'utf-8'.
        mode (str, optional): The file write mode. Defaults to 'w' (write).

    Raises:
        TypeError: If content is not a string or file_path is not a string.
        ValueError: If file_path is empty.
        IOError: If there are issues writing to the file.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(content, str):
        raise TypeError("content must be a string")
    
    # Validate file path
    if not file_path:
        raise ValueError("file_path cannot be empty")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
    
    # Write to file
    try:
        with open(file_path, mode, encoding=encoding) as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {e}")
    
    return True  # Indicate successful write
def extract_unique_chars(input_string):
    """
    Extract unique characters from a string without using built-in unique methods.
    
    Args:
        input_string (str): A string of characters to extract unique characters from.
    
    Returns:
        str: A string containing only the unique characters in the order of first appearance.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return ""
    
    # Use a custom method to track unique characters while preserving order
    result = []
    seen = set()
    
    for char in input_string:
        # Try to convert to numeric, skip non-numeric
        try:
            int(char)
        except ValueError:
            continue
        
        # Check if character is unique
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    # Convert result to string
    return ''.join(result)
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
    
    # Use a flag array to track character presence
    # Assume input is numeric, so we'll use a fixed-size flag array
    seen = [False] * 10
    result = []
    
    # Iterate through the input string
    for char in input_string:
        # Convert character to integer index
        try:
            index = int(char)
        except ValueError:
            # Skip non-numeric characters
            continue
        
        # If character hasn't been seen before, add to result
        if not seen[index]:
            seen[index] = True
            result.append(char)
    
    # Convert result to string
    return ''.join(result)
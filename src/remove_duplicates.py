def remove_duplicate_chars(input_string: str) -> str:
    """
    Remove duplicate characters from a lowercase input string.

    Args:
        input_string (str): A string containing only lowercase characters.

    Returns:
        str: A string with duplicate characters removed, preserving 
             the first occurrence of each character.

    Raises:
        ValueError: If the input contains non-lowercase characters.

    Examples:
        >>> remove_duplicate_chars("hello")
        'helo'
        >>> remove_duplicate_chars("aabbcc")
        'abc'
        >>> remove_duplicate_chars("")
        ''
    """
    # Handle empty string case explicitly
    if not input_string:
        return ""
    
    # Validate input is lowercase
    if not input_string.islower():
        raise ValueError("Input must contain only lowercase characters")
    
    # Use a set to track seen characters while preserving order
    seen = set()
    result = []
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)
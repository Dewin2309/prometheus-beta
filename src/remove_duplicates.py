def remove_duplicates_over_two(input_string: str) -> str:
    """
    Remove characters that appear more than twice in the input string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A string with characters appearing only once or twice.
    
    Examples:
        >>> remove_duplicates_over_two("aabbbcccc")
        'aabbcc'
        >>> remove_duplicates_over_two("python")
        'python'
        >>> remove_duplicates_over_two("")
        ''
    """
    if not input_string:
        return ""
    
    # Count the occurrences of each character
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Build the result string, keeping characters that appear 1 or 2 times
    result = ''.join(char for char in input_string 
                     if char_counts[char] <= 2)
    
    return result
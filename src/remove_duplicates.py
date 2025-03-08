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
    
    # Track the occurrences of each character
    result = []
    char_counts = {}
    
    for char in input_string:
        # If the character has appeared less than 2 times, add it
        if char_counts.get(char, 0) < 2:
            result.append(char)
            char_counts[char] = char_counts.get(char, 0) + 1
    
    return ''.join(result)
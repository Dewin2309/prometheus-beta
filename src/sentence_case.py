def to_sentence_case(input_string: str) -> str:
    """
    Convert a string to sentence case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to sentence case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_sentence_case("hello WORLD")
        'Hello world'
        >>> to_sentence_case("PYTHON is AWESOME")
        'Python is awesome'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Capitalize the first character and lowercase the rest
    return input_string[0].upper() + input_string[1:].lower()
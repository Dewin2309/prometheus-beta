def convert_to_alternating_case(input_string):
    """
    Convert a string to alternating lower case.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: A string with alternating lower case characters.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to alternating lower case with proper indexing
    result = []
    alpha_index = 0
    for char in input_string:
        if char.isalpha():
            # Use alpha_index for alphabetic characters to track alternation
            result.append(char.lower() if alpha_index % 2 == 0 else char.upper())
            alpha_index += 1
        else:
            # Non-alphabetic characters are added as-is without changing the alpha_index
            result.append(char)
    
    return ''.join(result)
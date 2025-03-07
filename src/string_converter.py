def to_camel_case(text: str) -> str:
    """
    Convert a string to camel case.
    
    Handles various input formats including snake_case, kebab-case, and space-separated words.
    Preserves capitalization of the first letter based on the input style.
    
    Args:
        text (str): The input string to convert to camel case.
    
    Returns:
        str: The camel case version of the input string.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_camel_case("hello world")
        'helloWorld'
        >>> to_camel_case("hello_world")
        'helloWorld'
        >>> to_camel_case("Hello-world")
        'helloWorld'
        >>> to_camel_case("Hello_World")
        'helloWorld'
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If the string is empty, return empty string
    if not text:
        return ""
    
    # Replace hyphens and underscores with spaces
    normalized = text.replace('-', ' ').replace('_', ' ')
    
    # Split the string maintaining numbers as part of words
    words = []
    current_word = ""
    for char in normalized:
        if char.isalpha():
            current_word += char
        elif char.isdigit():
            # If current word is not empty, append it and start a new word with number
            if current_word:
                words.append(current_word)
                current_word = ""
            current_word += char
        else:  # Whitespace or other separators
            if current_word:
                words.append(current_word)
                current_word = ""
    
    # Append the last word if it exists
    if current_word:
        words.append(current_word)
    
    # If no words, return empty string
    if not words:
        return ""
    
    # Convert to camel case
    # First word is always lowercase (unless it starts with uppercase)
    camel_words = [words[0].lower()]
    
    # Capitalize subsequent words
    camel_words.extend(word.capitalize() for word in words[1:])
    
    # Join the words
    return ''.join(camel_words)
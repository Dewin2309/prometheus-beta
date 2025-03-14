def is_palindrome(s: str) -> bool:
    """
    Determine if the given string is a palindrome.

    A palindrome reads the same backward as forward, ignoring case, 
    whitespace, and punctuation.

    Args:
        s (str): The input string to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("Was it a car or a cat I saw?")
        True
        >>> is_palindrome("hello")
        False
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]
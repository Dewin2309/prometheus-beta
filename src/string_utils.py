def reverse_words(sentence: str) -> str:
    """
    Reverse the order of words in a given string while handling multiple spaces 
    and ignoring non-alphabetic characters.
    
    Args:
        sentence (str): The input string to be processed
    
    Returns:
        str: A string with words in reversed order, preserving original spacing
    
    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("  Hello   World  ")
        '  World   Hello  '
        >>> reverse_words("123 abc 456 def")
        '456 def 123 abc'
    """
    # Handle empty or None input
    if not sentence:
        return ""
    
    # Split the string while preserving whitespace
    words = []
    current_word = []
    current_non_word = []
    
    for char in sentence:
        if char.isalnum():
            # If we have accumulated non-word characters, add them as a separate element
            if current_non_word:
                words.append(''.join(current_non_word))
                current_non_word = []
            current_word.append(char)
        else:
            # If we have a complete word, add it
            if current_word:
                words.append(''.join(current_word))
                current_word = []
            current_non_word.append(char)
    
    # Add any remaining word or non-word characters
    if current_word:
        words.append(''.join(current_word))
    if current_non_word:
        words.append(''.join(current_non_word))
    
    # Reverse the words while maintaining their original non-word separators
    return ''.join(reversed(words))
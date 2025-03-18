def reverse_words(sentence: str) -> str:
    """
    Reverse the order of words in a given string while handling multiple spaces 
    and preserving original formatting.
    
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
    
    # Split the string into tokens, preserving all whitespace and non-alphanumeric characters
    def tokenize(s):
        tokens = []
        current_token = []
        for char in s:
            if char.isalnum():
                current_token.append(char)
            else:
                if current_token:
                    tokens.append(''.join(current_token))
                    current_token = []
                tokens.append(char)
        if current_token:
            tokens.append(''.join(current_token))
        return tokens
    
    # Tokenize the input
    tokens = tokenize(sentence)
    
    # Separate alphanumeric words and non-word tokens
    words = [t for t in tokens if any(c.isalnum() for c in t)]
    non_word_tokens = [t for t in tokens if not any(c.isalnum() for c in t)]
    
    # Reverse the words
    reversed_words = list(reversed(words))
    
    # Reconstruct the string
    result = []
    word_index = 0
    token_index = 0
    
    while token_index < len(tokens):
        if tokens[token_index].isalnum():
            result.append(reversed_words[word_index])
            word_index += 1
        else:
            result.append(tokens[token_index])
        token_index += 1
    
    return ''.join(result)
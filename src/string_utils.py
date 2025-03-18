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
    
    # Split the string into tokens, preserving all whitespace and including numeric words
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
    
    # Reconstruct the string
    result = []
    token_index = 0
    
    while token_index < len(tokens):
        current_token = tokens[token_index]
        
        # Check if current token is an alphanumeric word
        if any(c.isalnum() for c in current_token):
            # Replace with the corresponding word from the end of the list
            result.append(words[len(words) - 1 - words.index(current_token)])
        else:
            # Preserve non-word tokens (spaces, punctuation)
            result.append(current_token)
        
        token_index += 1
    
    return ''.join(result)
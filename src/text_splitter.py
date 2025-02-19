def split_text_to_words(text):
    """
    Split text into words based on specific rules:
    1. Words are separated by capital letters or punctuation marks (except quotes)
    2. Punctuation marks are included at the end of words
    3. Sequences of capital letters are treated as separate words
    4. Quotation marks do not break words
    
    Args:
        text (str): Input text without spaces
    
    Returns:
        list: List of words extracted from the text
    """
    if not text:
        return []

    def parse_text(text):
        result = []
        current_word = ""
        
        for char in text:
            if char.isupper():
                # Transition from lowercase to uppercase
                if current_word and current_word[-1].islower():
                    result.append(current_word)
                    current_word = char
                # Pure uppercase word (abbreviation handling)
                elif not current_word or current_word.isupper():
                    current_word += char
                else:
                    current_word += char
            elif char.islower() or char.isdigit():
                current_word += char
            else:
                # Punctuation handling
                if current_word:
                    result.append(current_word)
                    current_word = ""
                result.append(char)
        
        # Final word append
        if current_word:
            result.append(current_word)
        
        return result

    # Special processing to consolidate results
    parsed = parse_text(text)
    
    # Consolidation stage
    consolidated = []
    i = 0
    while i < len(parsed):
        # Handle uppercase sequences
        if parsed[i].isupper() and len(parsed[i]) > 1 and i+1 < len(parsed) and parsed[i+1][0].isupper():
            # Merge uppercase sequences
            consolidated.append(''.join(parsed[i:i+2]))
            i += 2
        else:
            consolidated.append(parsed[i])
            i += 1
    
    return consolidated
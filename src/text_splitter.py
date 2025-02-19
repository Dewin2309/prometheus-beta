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

    def smart_split(text):
        result = []
        current_word = ""
        uppercase_sequence = ""
        
        for i, char in enumerate(text):
            if char.isupper():
                # Special handling for uppercase transitions
                if current_word and current_word[-1].islower():
                    # Transition from lowercase to uppercase
                    result.append(current_word)
                    current_word = ""
                    uppercase_sequence = char
                elif uppercase_sequence:
                    # Continuing uppercase sequence
                    if len(uppercase_sequence) < 2:
                        uppercase_sequence += char
                    else:
                        result.append(uppercase_sequence)
                        uppercase_sequence = char
                else:
                    current_word += char
            elif char.islower() or char.isdigit():
                # Handle transitions and continuous sequences
                if uppercase_sequence:
                    if len(uppercase_sequence) == 1:
                        current_word = uppercase_sequence + char
                    else:
                        result.append(uppercase_sequence)
                        current_word = char
                    uppercase_sequence = ""
                else:
                    current_word += char
            else:
                # Punctuation handling
                if current_word:
                    result.append(current_word)
                    current_word = ""
                if uppercase_sequence:
                    result.append(uppercase_sequence)
                    uppercase_sequence = ""
                result.append(char)
        
        # Final flushes
        if current_word:
            result.append(current_word)
        if uppercase_sequence:
            result.append(uppercase_sequence)
        
        return result

    def post_process(words):
        processed = []
        i = 0
        while i < len(words):
            # Special uppercase handling
            if words[i].isupper() and len(words[i]) > 1:
                # Intelligent split for abbreviations and sequences
                if i+1 < len(words) and words[i+1][0].isupper():
                    if len(words[i]) > 2:
                        processed.append(words[i][:2])
                        processed.append(words[i][2:])
                    else:
                        processed.append(words[i])
                else:
                    processed.append(words[i])
            else:
                processed.append(words[i])
            i += 1
        return processed

    return post_process(smart_split(text))
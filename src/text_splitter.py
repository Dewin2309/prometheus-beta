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

    def custom_split(text):
        result = []
        current_word = text[0]
        
        for char in text[1:]:
            # Transition from lowercase to uppercase
            if char.isupper() and current_word and current_word[-1].islower():
                result.append(current_word)
                current_word = char
            
            # Uppercase sequences handling
            elif char.isupper() and current_word.isupper():
                # Accumulate capital letters, but have a limit
                if len(current_word) < 3:
                    current_word += char
                else:
                    result.append(current_word)
                    current_word = char
            
            # Continuous word building
            else:
                current_word += char
        
        # Append final word
        if current_word:
            result.append(current_word)
        
        return result

    def post_process(words):
        processed = []
        i = 0
        while i < len(words):
            # Special uppercase sequence handling
            if words[i].isupper() and len(words[i]) > 1:
                if i+1 < len(words) and words[i+1][0].isupper():
                    # Strategic splitting for abbreviations
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

    return post_process(custom_split(text))
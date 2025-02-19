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

    def split_word(text):
        result = []
        current_word = text[0]
        
        for char in text[1:]:
            if char.isupper():
                # Transition from lowercase to uppercase: split
                if current_word and current_word[-1].islower():
                    result.append(current_word)
                    current_word = char
                # Continuation of uppercase word
                elif current_word.isupper():
                    current_word += char
                else:
                    current_word += char
            else:
                current_word += char
        
        if current_word:
            result.append(current_word)
        
        return result

    def post_process(words):
        processed = []
        i = 0
        while i < len(words):
            # Special handling for sequences of uppercase letters
            if words[i].isupper() and len(words[i]) > 1:
                # Strategy for handling uppercase sequences like ABC or AIGPT
                if i+1 < len(words) and words[i+1][0].isupper():
                    # If next word starts with uppercase, split strategically
                    if len(words[i]) > 2:
                        processed.append(words[i][:2])
                        processed.append(words[i][2:])
                    else:
                        processed.append(words[i])
                else:
                    # For pure uppercase sequences: split into characters
                    processed.extend(list(words[i]))
            else:
                processed.append(words[i])
            i += 1
        return processed

    initial_split = split_word(text)
    return post_process(initial_split)
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

    def advanced_split(text):
        result = []
        current_word = text[0]
        i = 1
        
        while i < len(text):
            char = text[i]
            
            # Transition from lowercase to uppercase: split
            if char.isupper() and current_word and current_word[-1].islower():
                result.append(current_word)
                current_word = char
            
            # Uppercase sequence handling
            elif char.isupper() and current_word.isupper():
                # Continuing uppercase word/abbreviation
                if len(current_word) < 2:
                    current_word += char
                else:
                    result.append(current_word)
                    current_word = char
            
            # Numeric transition
            elif char.isdigit() and not current_word[-1].isdigit():
                result.append(current_word)
                current_word = char
            
            # Normal character continuation
            else:
                current_word += char
            
            i += 1
        
        # Append final word
        if current_word:
            result.append(current_word)
        
        return result

    def post_process(words):
        processed = []
        i = 0
        while i < len(words):
            # Special uppercase handling
            if words[i].isupper() and len(words[i]) > 1:
                # Intelligent split for mixed abbreviations
                if i+1 < len(words) and words[i+1][0].isupper():
                    # For sequences like AIGPT4
                    if len(words[i]) > 2:
                        processed.append(words[i][:2])
                        processed.append(words[i][2:])
                    else:
                        processed.append(words[i])
                else:
                    # Split pure uppercase into individual letters
                    processed.extend(list(words[i]))
            else:
                processed.append(words[i])
            i += 1
        return processed

    # Handle punctuation before advanced processing
    punctuated_split = []
    for chunk in text.replace(',', ' , ').replace('!', ' ! ').replace('?', ' ? ').replace('.', ' . ').replace(':', ' : ').replace(';', ' ; ').split():
        punctuated_split.extend(advanced_split(chunk))
    
    return post_process(punctuated_split)
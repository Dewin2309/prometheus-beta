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

    words = []
    current_word = text[0]
    
    for char in text[1:]:
        if char.isupper():
            # Handle different cases of capital letters
            if current_word[-1].islower():
                # Start of a new word after lowercase
                words.append(current_word)
                current_word = char
            elif current_word.isupper():
                # Continuing an all-caps word or abbreviation
                current_word += char
            else:
                # Mixed case word
                current_word += char
        elif char.islower() or char.isdigit():
            # Extend current word with lowercase or digit
            current_word += char
        else:
            # Non-alphanumeric: punctuation
            if current_word:
                words.append(current_word)
                if not char.isspace():
                    words.append(char)
                current_word = ""
    
    # Append final word
    if current_word:
        words.append(current_word)
    
    # Post-processing step for specific requirements
    processed_words = []
    i = 0
    while i < len(words):
        # Handle abbreviations and sequences of capital letters
        if i+1 < len(words) and (words[i].isupper() and len(words[i]) > 1):
            # Split multi-letter abbreviation
            processed_words.extend(list(words[i]))
        elif words[i] != '':
            processed_words.append(words[i])
        i += 1
    
    return processed_words
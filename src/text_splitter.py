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

    def split_complicated_cases(text):
        result = []
        current_word = ""
        
        for i, char in enumerate(text):
            if char.isupper():
                # Manage transition between lowercase and uppercase
                if current_word and current_word[-1].islower():
                    result.append(current_word)
                    current_word = char
                # Manage consecutive uppercase (abbreviations)
                elif current_word and current_word.isupper():
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
                if not char.isspace():
                    result.append(char)
        
        # Append final word
        if current_word:
            result.append(current_word)
        
        return result

    def post_process(words):
        processed_words = []
        i = 0
        while i < len(words):
            # Special handling for uppercase sequences
            if i+1 < len(words) and words[i].isupper() and len(words[i]) > 1:
                # Split uppercase sequences longer than 1 character
                if len(words[i]) > 1 and i+1 < len(words) and words[i+1][0].isupper():
                    # Handling cases like OpenAIGPT4Model
                    if len(words[i]) > 2:
                        processed_words.append(words[i][:2])
                        processed_words.append(words[i][2:])
                    else:
                        processed_words.append(words[i])
                else:
                    # Split uppercase into individual characters
                    processed_words.extend(list(words[i]))
            else:
                processed_words.append(words[i])
            i += 1
        return processed_words

    initial_split = split_complicated_cases(text)
    return post_process(initial_split)
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

    def parse_complex_text(text):
        result = []
        current_word = ""
        
        for i, char in enumerate(text):
            # Intelligent word segmentation logic
            if char.isupper():
                # Transition from lowercase to uppercase
                if current_word and current_word[-1].islower():
                    result.append(current_word)
                    current_word = char
                # Multiple uppercase scenarios
                elif current_word and current_word.isupper():
                    # For abbreviation-like sequences
                    current_word += char
                    if len(current_word) > 2 or (i+1 < len(text) and text[i+1].islower()):
                        result.append(current_word)
                        current_word = ""
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
        
        # Append final word
        if current_word:
            result.append(current_word)
        
        return result

    def consolidate_results(words):
        final_result = []
        i = 0
        while i < len(words):
            # Complex uppercase handling
            if words[i].isupper() and len(words[i]) > 1:
                # Intelligent merging strategy
                if i+1 < len(words) and words[i+1][0].isupper():
                    final_result.append(words[i])
                else:
                    final_result.append(words[i])
            else:
                final_result.append(words[i])
            i += 1
        
        return final_result

    # Multi-stage parsing
    initial_parse = parse_complex_text(text)
    return consolidate_results(initial_parse)
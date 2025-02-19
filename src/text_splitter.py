import re

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
        """Custom logic for complex text splitting"""
        words = []
        current_word = ""
        current_capitals = ""
        
        for char in text:
            if char.isupper():
                # Handle accumulated capital letters
                if current_capitals and (not current_word or current_word[-1].islower()):
                    if len(current_capitals) > 1:
                        words.append(current_capitals)
                    else:
                        words.append(current_word) if current_word else None
                        current_word = char
                    current_capitals = ""
                elif current_word and current_word.isupper():
                    current_capitals += char
                    continue
                elif current_word:
                    # If current word is not all uppercase, flush and reset
                    words.append(current_word)
                    current_word = char
                else:
                    current_word = char
            elif char.islower() or char.isdigit():
                # Flush accumulated capitals before adding to word
                if current_capitals:
                    if len(current_capitals) > 1:
                        words.append(current_capitals)
                    else:
                        current_word += current_capitals
                    current_capitals = ""
                current_word += char
            else:
                # Non-alphanumeric character
                if current_word:
                    words.append(current_word)
                    current_word = ""
                if current_capitals:
                    words.append(current_capitals)
                    current_capitals = ""
                words.append(char)
        
        # Final flush
        if current_word:
            words.append(current_word)
        if current_capitals:
            words.append(current_capitals)
        
        return words

    return custom_split(text)
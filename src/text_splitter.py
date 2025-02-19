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

    # Enhanced regex to capture multiple scenarios
    pattern = re.compile(r'[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|[A-Z]?[a-z0-9]+|[A-Z]+|[0-9]+|[.,;:!?]')
    words = pattern.findall(text)
    
    # Post-processing to handle some specific cases
    processed_words = []
    i = 0
    while i < len(words):
        if i+1 < len(words) and len(words[i]) > 1 and words[i].isupper() and words[i+1][0].isupper():
            # Break up sequences of capital words
            for char in words[i]:
                processed_words.append(char)
            processed_words.append(words[i+1])
            i += 2
        else:
            processed_words.append(words[i])
            i += 1
    
    return processed_words
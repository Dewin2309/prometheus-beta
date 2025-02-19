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

    # Special regex to handle the splitting rules
    # Positive lookahead and lookbehind to preserve punctuation and capital letter splits
    words = re.findall(
        r'([A-Z]*[a-z0-9]+[.,;:!?]*' +  # Lowercase words with optional punc
        r'|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)' +  # Sequences of capital letters
        r'|[.,;:!?]+)', 
        text
    )
    
    return words
def switch_cases(str1, str2):
    """
    Swap the character cases between two input strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: A new string with characters from both inputs having their cases swapped
    
    Raises:
        TypeError: If either input is not a string
        ValueError: If input strings are of unequal length
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")
    
    # Ensure the strings are the same length
    if len(str1) != len(str2):
        raise ValueError("Input strings must be of equal length")
    
    # Create the new string with specific case transformation
    switched = ''
    for i in range(len(str1)):
        # Process first string's characters
        if str1[i].isupper():
            switched += str1[i].lower()
        else:
            switched += str1[i].upper()
        
        # Process second string's characters
        if str2[i].isupper():
            switched += str2[i].lower()
        else:
            switched += str2[i].upper()
    
    return switched
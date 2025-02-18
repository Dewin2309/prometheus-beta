def burrows_wheeler_transform(text):
    """
    Perform Burrows-Wheeler Transform on the input text.
    
    Args:
        text (str): Input text to transform
    
    Returns:
        tuple: A tuple containing the transformed text and the original index
    """
    # Handle empty string case
    if not text:
        return '', 0
    
    # Add a terminator character that is not in the text
    terminator = '$'
    text += terminator
    
    # Generate all rotations of the text
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    
    # Sort the rotations lexicographically 
    sorted_rotations = sorted(rotations)
    
    # Find the original index and create the transformed text
    original_index = sorted_rotations.index(text)
    transformed_text = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return transformed_text, original_index

def inverse_burrows_wheeler_transform(transformed_text, original_index):
    """
    Reverse the Burrows-Wheeler Transform.
    
    Args:
        transformed_text (str): Transformed text from BWT
        original_index (int): Original index from BWT
    
    Returns:
        str: Original text before transformation
    """
    # Handle empty string case
    if not transformed_text:
        return ''
    
    # Create First and Last columns
    n = len(transformed_text)
    first_column = sorted(transformed_text)
    
    # Create next array to reconstruct the original text
    next_array = [0] * n
    used = [False] * n
    
    for i in range(n):
        count = 0
        for j in range(n):
            if not used[j] and first_column[j] == transformed_text[i]:
                next_array[i] = j
                used[j] = True
                break
    
    # Reconstruct the original text
    result = []
    current_index = original_index
    for _ in range(n - 1):  # Exclude the terminator
        result.append(transformed_text[current_index])
        current_index = next_array[current_index]
    
    return ''.join(result).rstrip('$')
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
    extended_text = text + terminator
    
    # Generate all rotations of the text
    rotations = [extended_text[i:] + extended_text[:i] for i in range(len(extended_text))]
    
    # Sort the rotations lexicographically 
    sorted_rotations = sorted(rotations)
    
    # Find the original index and create the transformed text
    original_index = sorted_rotations.index(extended_text)
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
    position_in_first = {}
    
    # Count occurrences of each character to handle repeated chars
    for i, char in enumerate(first_column):
        if char not in position_in_first:
            position_in_first[char] = 0
        position_in_first[char] += 1
    
    # Track last seen position for each unique character
    last_seen = {char: 0 for char in set(first_column)}
    
    for i in range(n):
        current_char = transformed_text[i]
        count = last_seen.get(current_char, 0)
        
        # Find the corresponding position in the first column
        for j in range(n):
            if first_column[j] == current_char and count == 0:
                next_array[i] = j
                last_seen[current_char] = count + 1
                break
            elif first_column[j] == current_char:
                count -= 1
    
    # Reconstruct the original text
    result = []
    current_index = original_index
    
    for _ in range(n - 1):  # Exclude the terminator
        result.append(transformed_text[current_index])
        current_index = next_array[current_index]
    
    return ''.join(result)[:-1]  # Remove terminator
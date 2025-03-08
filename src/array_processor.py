def process_multidim_array(arr):
    """
    Process a multi-dimensional array by:
    1. Removing empty sub-arrays
    2. Reversing the order of elements in each sub-array
    3. Flattening the array
    4. Removing duplicates while maintaining original order

    Args:
        arr (list): A multi-dimensional input array

    Returns:
        list: Processed array with duplicates removed
    """
    # Remove empty sub-arrays
    non_empty_arrays = [subarray for subarray in arr if subarray]
    
    # Reverse elements in each sub-array
    reversed_arrays = [list(reversed(subarray)) for subarray in non_empty_arrays]
    
    # Flatten the array
    flattened = [item for subarray in reversed_arrays for item in subarray]
    
    # Remove duplicates while maintaining order
    seen = set()
    unique_result = []
    for item in flattened:
        if item not in seen:
            unique_result.append(item)
            seen.add(item)
    
    return unique_result
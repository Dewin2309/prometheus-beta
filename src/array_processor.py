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
    def deep_flatten(item):
        """Recursively flatten nested lists."""
        if not isinstance(item, list):
            return [item]
        flattened = []
        for subitem in item:
            flattened.extend(deep_flatten(subitem))
        return flattened

    # Remove empty sub-arrays
    non_empty_arrays = [subarray for subarray in arr if subarray]
    
    # Processing for each subarray
    processed_arrays = []
    for subarray in non_empty_arrays:
        # Reverse the subarray and deeply flatten
        reversed_subarray = list(reversed(subarray))
        processed_arrays.extend(deep_flatten(reversed_subarray))
    
    # Remove duplicates while maintaining order of first occurrence
    seen = set()
    unique_result = []
    for item in processed_arrays:
        if item not in seen:
            unique_result.append(item)
            seen.add(item)
    
    return unique_result
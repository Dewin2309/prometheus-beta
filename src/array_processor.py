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
    def process_subarray(subarray):
        """Process a single subarray by reversing it and deeply flattening."""
        if not subarray:
            return []
        
        # Reverse the subarray
        reversed_subarray = list(reversed(subarray))
        
        # Deep flatten
        def flatten(item):
            if not isinstance(item, list):
                return [item]
            
            flat_result = []
            for sub_item in item:
                flat_result.extend(flatten(sub_item))
            return flat_result
        
        return flatten(reversed_subarray)

    # Remove empty sub-arrays and process from the end
    non_empty_arrays = [subarray for subarray in arr if subarray]
    
    # Process and flatten each subarray
    flattened = []
    for subarray in reversed(non_empty_arrays):
        flattened.extend(process_subarray(subarray))
    
    # Remove duplicates while maintaining order of first occurrence
    seen = set()
    unique_result = []
    for item in flattened:
        if item not in seen:
            unique_result.append(item)
            seen.add(item)
    
    return unique_result
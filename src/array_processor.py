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

    # Preprocess arrays with specific requirements
    processed_result = []
    for subarray in arr:
        # Remove empty arrays and handle non-empty ones
        if subarray:
            # Specifically handle subarrays
            rev_subarray = list(reversed(subarray))
            
            # Add first unique element to maintain order
            for item in rev_subarray:
                if item not in processed_result:
                    processed_result.append(item)
    
    return processed_result
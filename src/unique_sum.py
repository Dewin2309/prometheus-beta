def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): An array of integers
    
    Returns:
        int: Sum of unique elements in the array
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If input is not a list
        TypeError: If list contains non-integer elements
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Use a set to track unique elements
    unique_elements = set()
    
    # Use a set to track duplicates
    duplicates = set()
    
    # Iterate through the array once
    for num in arr:
        # If number is already in unique_elements, it's a duplicate
        if num in unique_elements:
            duplicates.add(num)
        else:
            unique_elements.add(num)
    
    # Calculate sum of unique elements (those not in duplicates)
    return sum(num for num in unique_elements if num not in duplicates)
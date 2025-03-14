def find_first_occurrence(arr, target):
    """
    Find the index of the first occurrence of a target number in a sorted array using binary search.
    
    Args:
        arr (list): A sorted array of positive integers
        target (int): The number to find in the array
    
    Returns:
        int: Index of the first occurrence of the target, or -1 if not found
    
    Raises:
        TypeError: If input is not a list or target is not an integer
        ValueError: If array contains non-positive integers
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check if all elements are positive integers
    if any(not isinstance(x, int) or x <= 0 for x in arr):
        raise ValueError("Array must contain only positive integers")
    
    # Binary search implementation
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Found a match, but continue searching left for first occurrence
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            # Target is in the right half
            left = mid + 1
        else:
            # Target is in the left half
            right = mid - 1
    
    return result
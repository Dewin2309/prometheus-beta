from typing import List, Any

def library_sort(arr: List[Any]) -> List[Any]:
    """
    Implement the Library Sort algorithm (Insertion Sort with gaps).
    
    Library Sort is a variant of insertion sort that uses a logarithmic number 
    of gaps to improve average-case performance compared to standard insertion sort.
    
    Args:
        arr (List[Any]): The input list to be sorted
    
    Returns:
        List[Any]: A sorted list in ascending order
    
    Time Complexity: 
        - Best Case: O(n)
        - Average Case: O(n log n)
        - Worst Case: O(n^2)
    
    Space Complexity: O(n)
    
    Raises:
        TypeError: If input is not a list
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a list with exponentially increasing gaps
    sorted_arr = [None] * (len(arr) * 2 + 1)
    
    # Place the first element
    sorted_arr[len(arr)] = arr[0]
    
    # Process remaining elements
    for i in range(1, len(arr)):
        current = arr[i]
        
        # Find insertion point
        j = len(arr)
        while True:
            # Move left or right to find appropriate gap
            if sorted_arr[j] is None:
                sorted_arr[j] = current
                break
            
            # Compare and shift if needed
            if current < sorted_arr[j]:
                j -= 1
            else:
                j += 1
    
    # Remove None values and return
    return [x for x in sorted_arr if x is not None]
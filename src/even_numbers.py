def extract_even_numbers(sorted_nums):
    """
    Extract even numbers from a sorted list of unique integers while maintaining their original order.

    Args:
        sorted_nums (list): A sorted list of unique integers.

    Returns:
        list: A new list containing only the even numbers from the input list.

    Time Complexity: O(n) - single pass through the input list
    Space Complexity: O(n) in the worst case where all numbers are even

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is not sorted or contains duplicates.
    """
    # Type checking
    if not isinstance(sorted_nums, list):
        raise TypeError("Input must be a list")
    
    # Validate sorted and unique property
    if len(sorted_nums) != len(set(sorted_nums)) or sorted_nums != sorted(sorted_nums):
        raise ValueError("Input must be a sorted list of unique integers")
    
    # Extract even numbers in O(n) time
    return [num for num in sorted_nums if num % 2 == 0]
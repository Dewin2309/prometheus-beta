def find_non_overlapping_palindromes(s):
    """
    Find all non-overlapping palindromic substrings in the input string.
    
    Args:
        s (str): Input string to find palindromic substrings
    
    Returns:
        list: Sorted list of unique non-overlapping palindromic substrings
    """
    if not s:
        return []
    
    # Helper function to check if a substring is a palindrome
    def is_palindrome(substr):
        return substr == substr[::-1]
    
    # Find non-overlapping palindromic substrings
    palindromes = set()
    n = len(s)
    
    # Track the last index processed to ensure non-overlapping
    last_processed_index = -1
    
    # Iterate through all possible palindrome lengths
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            # Skip if this substring would overlap with a previous one
            if start <= last_processed_index:
                continue
            
            substr = s[start:start+length]
            
            # Check if it's a palindrome
            if is_palindrome(substr):
                palindromes.add(substr)
                # Update last processed index
                last_processed_index = start + length - 1
    
    # Sort palindromes lexicographically
    return sorted(list(palindromes))
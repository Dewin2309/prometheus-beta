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
    
    # Find all possible palindromic substrings
    palindromes = []
    n = len(s)
    
    # Iterate through all possible substrings
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substr = s[start:start+length]
            if is_palindrome(substr) and substr not in palindromes:
                palindromes.append(substr)
    
    # Sort palindromes lexicographically
    return sorted(palindromes)
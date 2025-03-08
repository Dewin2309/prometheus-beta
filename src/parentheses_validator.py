def is_valid_parentheses(s: str) -> bool:
    """
    Determine if a string of parentheses is valid.
    
    A string is considered valid if:
    - Every opening parenthesis has a corresponding closing parenthesis
    - Parentheses are closed in the correct order
    
    Args:
        s (str): A string containing only parentheses '(' and ')'
    
    Returns:
        bool: True if the parentheses are valid, False otherwise
    
    Examples:
        >>> is_valid_parentheses("()")
        True
        >>> is_valid_parentheses("(())")
        True
        >>> is_valid_parentheses(")(")
        False
        >>> is_valid_parentheses("(()")
        False
    """
    # Track open parentheses
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        if char == '(':
            # Push opening parenthesis onto stack
            stack.append(char)
        elif char == ')':
            # If closing parenthesis and no matching open parenthesis, return False
            if not stack:
                return False
            
            # Remove the last open parenthesis
            stack.pop()
    
    # Return True only if all parentheses are matched (stack is empty)
    return len(stack) == 0
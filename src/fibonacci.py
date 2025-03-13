def extended_fibonacci(n):
    """
    Generate the nth number in the extended Fibonacci sequence, supporting negative indices and float inputs.
    
    The extended Fibonacci sequence allows negative indices and maintains the core Fibonacci recurrence 
    relation F(n) = F(n-1) + F(n-2) for all integers.
    
    Args:
        n (int or float): The index of the Fibonacci number to generate.
    
    Returns:
        float: The nth number in the extended Fibonacci sequence.
    
    Raises:
        TypeError: If the input is not a number.
    """
    # Check input type
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    
    # Handle integer cases first (including negative integers)
    if isinstance(n, int):
        # Use memoization to efficiently calculate Fibonacci numbers
        memo = {}
        
        def fib(k):
            # Handling base cases
            if k == 0:
                return 0
            if k == 1 or k == -1:
                return 1
            if k == -2:
                return -1
            
            # Check memoized results to avoid recomputation
            if k in memo:
                return memo[k]
            
            # Recursive calculation using the extended recurrence relation
            # Works for both positive and negative indices
            memo[k] = fib(k-1) + fib(k-2)
            return memo[k]
        
        return float(fib(n))
    
    # Handle float cases using interpolation
    # For non-integer inputs, we'll use linear interpolation between surrounding integers
    else:
        # Split the float into integer and fractional parts
        int_part = int(n)
        frac_part = n - int_part
        
        # Calculate surrounding integer Fibonacci numbers
        lower_fib = extended_fibonacci(int_part)
        upper_fib = extended_fibonacci(int_part + 1)
        
        # Linear interpolation
        return lower_fib + frac_part * (upper_fib - lower_fib)
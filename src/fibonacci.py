def extended_fibonacci(n):
    """
    Generate the nth number in the extended Fibonacci sequence, supporting 
    negative indices and float inputs.
    
    The extended Fibonacci sequence is defined with the recurrence relation 
    F(n) = F(n-1) + F(n-2) and some specific base cases for integer and 
    float inputs.
    
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
    
    # For integer inputs
    if isinstance(n, int):
        def fibonacci_iterative(k):
            """Compute Fibonacci numbers efficiently for integer inputs."""
            # Positive and negative base cases
            base_cases = {
                0: 0,
                1: 1,
                -1: 1,
                -2: -1
            }
            
            # Direct return for known base cases
            if k in base_cases:
                return base_cases[k]
            
            # Determine direction of computation
            steps = abs(k)
            sign = 1 if k >= 0 else (-1) ** (abs(k) + 1)
            
            # Initialize for computation
            if k > 0:
                a, b = 0, 1
                for _ in range(2, steps + 1):
                    a, b = b, a + b
                return b
            else:
                a, b = 1, -1
                for _ in range(2, steps + 1):
                    a, b = b, a - b
                return a * sign
        
        return float(fibonacci_iterative(n))
    
    # For float inputs
    else:
        # Integer and fractional parts
        int_part = int(n)
        frac_part = n - int_part
        
        # Compute surrounding integer Fibonacci numbers
        lower_fib = extended_fibonacci(int_part)
        upper_fib = extended_fibonacci(int_part + 1)
        
        # Linear interpolation
        return lower_fib + frac_part * (upper_fib - lower_fib)
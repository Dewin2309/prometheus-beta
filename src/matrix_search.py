def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (list[list[int]]): A 2D matrix of unique integers
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target is found, False otherwise
    
    Raises:
        ValueError: If the input matrix is empty or None
    
    Time Complexity: O(T * R), where T is the number of rows and R is the number of columns
    Space Complexity: O(1) as we're doing an in-place search
    """
    # Check for invalid input
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Linear search through the matrix
    for row in matrix:
        if target in row:
            return True
    
    return False
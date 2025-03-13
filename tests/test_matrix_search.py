import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic():
    """Test basic matrix search functionality"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 9) == True
    assert search_matrix(matrix, 8) == False

def test_matrix_search_single_row():
    """Test search in a single-row matrix"""
    matrix = [[1, 2, 3, 4, 5]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 6) == False

def test_matrix_search_single_column():
    """Test search in a single-column matrix"""
    matrix = [[1], [2], [3], [4], [5]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 6) == False

def test_matrix_search_edge_cases():
    """Test edge cases like empty matrix or extreme values"""
    with pytest.raises(ValueError):
        search_matrix([], 5)
    
    with pytest.raises(ValueError):
        search_matrix([[]], 5)

def test_matrix_search_large_matrix():
    """Test search in a larger matrix"""
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    assert search_matrix(matrix, 7) == True
    assert search_matrix(matrix, 17) == False

def test_matrix_search_negative_numbers():
    """Test search with negative numbers"""
    matrix = [
        [-5, -3, -1],
        [0, 2, 4],
        [6, 8, 10]
    ]
    assert search_matrix(matrix, -3) == True
    assert search_matrix(matrix, 5) == False
import pytest
from src.bfs import breadth_first_search

def test_basic_bfs():
    """Test basic BFS on a simple graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']

def test_single_node_graph():
    """Test BFS on a graph with a single node."""
    graph = {'A': []}
    result = breadth_first_search(graph, 'A')
    assert result == ['A']

def test_disconnected_graph():
    """Test BFS on a disconnected graph."""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_invalid_start_node():
    """Test that an error is raised when start node is not in graph."""
    graph = {'A': ['B'], 'B': ['A']}
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        breadth_first_search(graph, 'X')

def test_invalid_graph_type():
    """Test that an error is raised for invalid graph type."""
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        breadth_first_search([], 'A')

def test_graph_with_no_neighbors():
    """Test BFS on a graph where nodes have no neighbors."""
    graph = {
        'A': [],
        'B': [],
        'C': []
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A']
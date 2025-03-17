from collections import deque
from typing import List, Dict, Any, Optional

def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Breadth-First Search on a graph.

    Args:
        graph (Dict[Any, List[Any]]): A dictionary representing the graph 
            where keys are nodes and values are lists of adjacent nodes.
        start (Any): The starting node for the BFS traversal.

    Returns:
        List[Any]: A list of nodes in the order they were visited.

    Raises:
        ValueError: If the start node is not in the graph.
        TypeError: If the graph is not a valid dictionary.
    """
    # Validate input
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")
    
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    
    # Initialize 
    visited = []
    queue = deque([start])
    explored = set([start])
    
    # BFS traversal
    while queue:
        # Remove the first node from the queue
        current = queue.popleft()
        visited.append(current)
        
        # Explore neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in explored:
                explored.add(neighbor)
                queue.append(neighbor)
    
    return visited
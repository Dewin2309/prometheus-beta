class Queue:
    """
    A simple Queue implementation using a list.
    
    This Queue class provides basic operations like enqueue, dequeue, 
    and checking if the queue is empty.
    """
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self._items = []
    
    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self._items.append(item)
    
    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0


def is_word_valid(word, rules):
    """
    Determine if a given word is valid based on specified rules.
    
    Args:
        word (str): The word to validate.
        rules (dict): A dictionary of validation rules.
    
    Returns:
        bool: True if the word is valid, False otherwise.
    
    Raises:
        ValueError: If rules are improperly formatted.
    """
    # Validate input types
    if not isinstance(word, str):
        return False
    
    if not isinstance(rules, dict):
        raise ValueError("Rules must be a dictionary")
    
    # Default rule checks
    # Check minimum length
    min_length = rules.get('min_length', 0)
    if len(word) < min_length:
        return False
    
    # Check maximum length
    max_length = rules.get('max_length', float('inf'))
    if len(word) > max_length:
        return False
    
    # Check allowed characters
    allowed_chars = rules.get('allowed_chars')
    if allowed_chars is not None:
        # Create a set of allowed chars for efficient lookup
        allowed_set = set(allowed_chars)
        
        # If any character is NOT in the allowed set, return False
        for char in word:
            if char not in allowed_set:
                return False
    
    # Check prohibited characters
    prohibited_chars = rules.get('prohibited_chars', [])
    if any(char in prohibited_chars for char in word):
        return False
    
    # Check start/end character rules
    start_chars = rules.get('start_chars')
    if start_chars is not None and word[0] not in start_chars:
        return False
    
    end_chars = rules.get('end_chars')
    if end_chars is not None and word[-1] not in end_chars:
        return False
    
    # Optional custom validation function
    custom_validation = rules.get('custom_validation')
    if custom_validation is not None:
        return custom_validation(word)
    
    return True
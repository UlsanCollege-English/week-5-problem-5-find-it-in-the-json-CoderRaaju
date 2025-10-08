def find_key(data, key):
    """
    Depth-first left-to-right search for the first occurrence of key.
    Return value or None if not found.
    
    data: dict, list, tuple, or other
    key: string
    """
    if isinstance(data, dict):
        # Check current dict for key first
        if key in data:
            return data[key]
        # Recurse into values
        for value in data.values():
            found = find_key(value, key)
            if found is not None:
                return found
    elif isinstance(data, (list, tuple)):
        # Recurse into each element
        for item in data:
            found = find_key(item, key)
            if found is not None:
                return found
    # Not found or not a collection
    return None

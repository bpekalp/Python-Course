def getTodoIndex(_values, _key, _todos):
    """Gets the specified To-Do index and returns it.

    Args:
        _values (dict): The dictionary provided by window.read() function
        _key (str): A key of the dictionary
        _todos (list): To-Do list of the user

    Returns:
        int: Returns the index of a To-Do in To-Do list
    """
    todo = _values[_key][0]
    index = _todos.index(todo)
    return index

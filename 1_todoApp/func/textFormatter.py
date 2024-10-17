def textBoxToTodo(_value, _key):
    """Reads text box and formats the content before writing into todos file

    Args:
        _value (dict): The dictionary item provided by FreeSimpleGUI library.
        _key (str): The key of item.

    Returns:
        str: Returns the formatted To-Do item.
    """
    todo = str(_value[_key]).strip().title() + "\n"
    return todo

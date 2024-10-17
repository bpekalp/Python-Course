def updateTodoBox(_window, _key, _value):
    """Updates the contents of FreeEasyGUI window.

    Args:
        _window (FreeEasyGUI.window): Instance of a window.
        _key (str): Dictionary item inside the window instance.
        _value (list): List that will be inserted into window instance.
    """
    _window[_key].update(value=_value)


def updateTodoList(_window, _key, _value):
    """Updates the contents of FreeEasyGUI window.

    Args:
        _window (FreeEasyGUI.window): Instance of a window.
        _key (str): Dictionary item inside the window instance.
        _value (list): List that will be inserted into window instance.
    """
    _window[_key].update(values=_value)

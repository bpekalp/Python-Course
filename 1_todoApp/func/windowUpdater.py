def updateWindow(_window, _key, _type, _value):
    """_summary_

    Args:
        _window (FreeSimpleGUI.window): Instance of a window.
        _key (str): Dictionary item inside the window instance.
        _type (str): Determines the type of the window element to be updated.
        _value (list): List that will be inserted into window instance.
    """
    if _type == "list":
        _window[_key].update(values=_value)

    if _type == "text":
        _window[_key].update(value=_value)

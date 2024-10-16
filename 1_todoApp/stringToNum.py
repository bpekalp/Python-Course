def stringToNum(_option, _userIf):
    """Extracts the number from user's input. e.g:
    extracts the 14 from "edit 14" or 27 from "complete 27"

    Args:
        _option (str): Variable that contains the user's entire input. e.g "edit 14"
        _userIf (str): Variable that contains only the user's choice e.g "edit"

    Returns:
        int: Converts the extracted number from string to integer and returns it.
    """
    _numStr = _option.lstrip(_userIf).strip()
    _num = int(_numStr) - 1
    return _num

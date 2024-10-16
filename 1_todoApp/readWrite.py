def readTodos(_filePath):
    """Reads specified file and returns the content as a list.

    Args:
        _filePath (str): File path of the file that will be read.

    Returns:
        list: Returns a list that contains each line of the file as one member.
    """
    try:
        with open(_filePath, "r") as _file:
            _todos = _file.readlines()
        return _todos
    except FileNotFoundError:
        print("File not found. Creating one...")
        writeTodos([], _filePath)
        return []


def writeTodos(_todos, _filePath):
    """Writes the contents of the current To-Do list that the user sees
    into the specified file.

    Args:
        _todos (list): Variable that contains the members of To-Do list.
        _filePath (str): File path of the file that will be read.
    """
    with open(_filePath, "w") as _file:
        _file.writelines(_todos)


def main():
    print(f"readWrite's name is: {__name__}")


if __name__ == "__main__":
    main()

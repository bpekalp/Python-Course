todos = []

todoPrompt = "Enter a To-Do: "
optionPrompt = (
    "Usage: add <To-Do>, edit <To-Do number>, show, complete <To-Do number> or exit: "
)
numPrompt = "Got it. Which one? "

filePath = "data/.todos.txt"


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


def main():
    while True:
        option = input(optionPrompt).lower().strip()

        if option.startswith("add"):
            todos = readTodos(filePath)

            userIf = "add"
            todo = option.lstrip(userIf).strip().capitalize() + "\n"
            todos.append(todo)

            writeTodos(todos, filePath)

        elif option.startswith("edit"):
            try:
                todos = readTodos(filePath)

                userIf = "edit"
                num = stringToNum(option, userIf)

                todo = input(todoPrompt).strip().capitalize() + "\n"
                todos[num] = todo

                writeTodos(todos, filePath)

            except ValueError:
                message = "Usage: edit <To-Do number to edit>"
                print(message)
                continue

            except IndexError:
                message = "The number was out of bounds of the To-Do list."
                print(message)
                continue

        elif option.startswith("show"):
            todos = readTodos(filePath)

            # todos = [todo.strip("\n") for todo in todos]
            for i, todo in enumerate(todos, start=1):
                todo = todo.strip("\n")
                message = f"{i}. {todo}"
                print(message)

        elif option.startswith("complete"):
            try:
                todos = readTodos(filePath)

                userIf = "complete"
                num = stringToNum(option, userIf)

                todo = todos.pop(num).strip("\n")
                message = f"{todo} is marked as done and removed from the list."
                print(message)

                writeTodos(todos, filePath)

            except ValueError:
                message = "Usage: complete <To-Do number to complete>"
                print(message)
                continue

            except IndexError:
                message = "The number was out of bounds of the To-Do list."
                print(message)
                continue

        elif option.startswith("exit"):
            message = "Goodbye!"
            print(message)
            break

        else:
            message = "Wrong input, try again."
            print(message)


if __name__ == "__main__":
    main()

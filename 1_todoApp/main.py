todos = []

todoPrompt = "Enter a To-Do: "
optionPrompt = "Type add, edit, show, complete or exit: "
numPrompt = "Got it. Which one? "

filePath = "data/.todos.txt"


def getOptionFromUser(optionPrompt):
    option = input(optionPrompt).lower().strip()
    return option


def readTodos(filePath):
    with open(filePath, "r") as file:
        todos = file.readlines()
    return todos


def writeTodos(todos, filePath):
    with open(filePath, "w") as file:
        file.writelines(todos)


def getTodoFromUser(todoPrompt):
    todo = input(todoPrompt).capitalize().strip() + "\n"
    return todo


def getIndexFromUser(numPrompt):
    num = int(input(numPrompt)) - 1
    return num


def displayTodos(todos):
    # todos = [todo.strip("\n") for todo in todos]

    for i, todo in enumerate(todos, start=1):
        todo = todo.strip("\n")
        row = f"{i}. {todo}"
        print(row)


def popTodo(todos, num):
    todo = todos.pop(num).capitalize().strip("\n")
    return todo


while True:
    option = getOptionFromUser(optionPrompt)

    match option:
        case "add":
            todos = readTodos(filePath)

            todo = getTodoFromUser(todoPrompt)
            todos.append(todo)

            writeTodos(todos, filePath)

        case "edit":
            todos = readTodos(filePath)

            num = getIndexFromUser(numPrompt)
            todo = getTodoFromUser(todoPrompt)
            todos[num] = todo

            writeTodos(todos, filePath)

        case "show":
            todos = readTodos(filePath)
            displayTodos(todos)

        case "complete":
            todos = readTodos(filePath)

            num = getIndexFromUser(numPrompt)
            todo = popTodo(todos, num)
            row = f"{todo} is marked as done and removed from the list."
            print(row)

            writeTodos(todos, filePath)

        case "exit":
            break

        case _:
            row = "Wrong input, try again."
            print(row)

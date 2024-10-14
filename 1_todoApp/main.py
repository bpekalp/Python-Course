todos = []

todoPrompt = "Enter a To-Do: "
optionPrompt = "Type add, edit, show, complete or exit: "
numPrompt = "Got it. Which one? "

filePath = "data/.todos.txt"

while True:
    option = input(optionPrompt).lower().strip()

    if option.startswith("add"):
        with open(filePath, "r") as file:
            todos = file.readlines()

        userIf = "add"
        todo = option.lstrip(userIf).strip().capitalize() + "\n"
        todos.append(todo)

        with open(filePath, "w") as file:
            file.writelines(todos)

    elif option.startswith("edit"):
        try:
            with open(filePath, "r") as file:
                todos = file.readlines()

            userIf = "edit"
            numStr = option.lstrip(userIf).strip()
            num = int(numStr) - 1

            todo = input(todoPrompt).strip().capitalize() + "\n"
            todos[num] = todo

            with open(filePath, "w") as file:
                file.writelines(todos)
        except ValueError:
            message = "Usage: edit <To-Do number to edit>"
            print(message)
            continue

        except IndexError:
            message = "The number was out of bounds of the To-Do list."
            print(message)
            continue

    elif option.startswith("show"):
        with open(filePath, "r") as file:
            todos = file.readlines()

        # todos = [todo.strip("\n") for todo in todos]
        for i, todo in enumerate(todos, start=1):
            todo = todo.strip("\n")
            message = f"{i}. {todo}"
            print(message)

    elif option.startswith("complete"):
        try:
            with open(filePath, "r") as file:
                todos = file.readlines()

            userIf = "complete"
            numStr = option.lstrip(userIf).strip()
            num = int(numStr) - 1

            todo = todos.pop(num).strip("\n")
            message = f"{todo} is marked as done and removed from the list."
            print(message)

            with open(filePath, "w") as file:
                file.writelines(todos)

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

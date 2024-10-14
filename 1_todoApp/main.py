todos = []

todoPrompt = "Enter a To-Do: "
optionPrompt = "Type add, edit, show, complete or exit: "
numPrompt = "Got it. Which one? "

filePath = "data/.todos.txt"

while True:
    option = input(optionPrompt).lower().strip()

    if "add" in option:
        with open(filePath, "r") as file:
            todos = file.readlines()

        todo = option.lstrip("add").strip().capitalize() + "\n"
        todos.append(todo)

        with open(filePath, "w") as file:
            file.writelines(todos)

    elif "edit" in option:
        with open(filePath, "r") as file:
            todos = file.readlines()

        numStr = option.lstrip("edit").strip()
        num = int(numStr) - 1

        todo = input(todoPrompt).capitalize().strip() + "\n"
        todos[num] = todo

        with open(filePath, "w") as file:
            file.writelines(todos)

    elif "show" in option:
        with open(filePath, "r") as file:
            todos = file.readlines()

        # todos = [todo.strip("\n") for todo in todos]
        for i, todo in enumerate(todos, start=1):
            todo = todo.strip("\n")
            message = f"{i}. {todo}"
            print(message)

    elif "complete" in option:
        with open(filePath, "r") as file:
            todos = file.readlines()

        numStr = option.lstrip("complete").strip()
        num = int(numStr) - 1

        todo = todos.pop(num).strip("\n")
        message = f"{todo} is marked as done and removed from the list."
        print(message)

        with open(filePath, "w") as file:
            file.writelines(todos)

    elif "exit" in option:
        break

    else:
        message = "Wrong input, try again."
        print(message)

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
        num = int(input(numPrompt)) - 1
        todo = input(todoPrompt).capitalize().strip()
        todos[num] = todo

    elif "show" in option:
        with open(filePath, "r") as file:
            todos = file.readlines()

        # todos = [todo.strip("\n") for todo in todos]

        for i, todo in enumerate(todos, start=1):
            todo = todo.strip("\n")
            row = f"{i}. {todo}"
            print(row)

    elif "complete" in option:
        num = int(input(numPrompt)) - 1
        todo = todos.pop(num)
        row = f"{todo} is marked as done and removed from the list."
        print(row)

    elif "exit" in option:
        break

    else:
        row = "Wrong input, try again."
        print(row)

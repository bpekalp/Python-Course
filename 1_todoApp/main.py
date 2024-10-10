todos = []

todoPrompt = "Enter a To-Do: "
optionPrompt = "Type add, edit, show, complete or exit: "
numPrompt = "Got it. Which one? "

filePath = "data/.todos.txt"

while True:
    option = input(optionPrompt).lower().strip()

    match option:
        case "add":
            file = open(filePath, "r")
            todos = file.readlines()
            file.close()

            todo = input(todoPrompt).capitalize().strip() + "\n"
            todos.append(todo)

            file = open(filePath, "w")
            file.writelines(todos)
            file.close()

        case "edit":
            num = int(input(numPrompt)) - 1
            todo = input(todoPrompt).capitalize().strip()
            todos[num] = todo

        case "show":
            file = open(filePath, "r")
            todos = file.readlines()
            file.close()

            # todos = [todo.strip("\n") for todo in todos]

            for i, todo in enumerate(todos, start=1):
                todo = todo.strip("\n")
                row = f"{i}. {todo}"
                print(row)

        case "complete":
            num = int(input(numPrompt)) - 1
            todo = todos.pop(num)
            row = f"{todo} is marked as done and removed from the list."
            print(row)

        case "exit":
            break

        case _:
            row = "Wrong input, try again."
            print(row)

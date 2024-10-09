todos = []

todoPrompt = "Enter a To-Do: "
optionPrompt = "Type add, edit, show, complete or exit: "
numPrompt = "Got it. Which one? "

filePath = "data/.todos.txt"
file = open(filePath, "r")
file.close()

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

            for i, item in enumerate(todos, start=1):
                row = f"{i}. {item}"
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

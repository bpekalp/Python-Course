optionPrompt = "Type add, show or exit: "
option = ""

todoPrompt = "Enter a To-Do: "
todo = ""

todos = []

while True:
    option = input(optionPrompt).lower().strip()
    match option:
        case "add":
            todo = input(todoPrompt).capitalize().strip()
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
        case _:
            print("Wrong input, try again.")

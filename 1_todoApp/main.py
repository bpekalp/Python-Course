optionPrompt = "Type add, show or exit: "
option = ""

todoPrompt = "Enter a To-Do: "
todo = ""

todos = []

while True:
    option = input(optionPrompt)
    option = option.lower()
    match option:
        case "add":
            todo = input(todoPrompt)
            todo = todo.capitalize()
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
        case _:
            print("Wrong input, try again.")

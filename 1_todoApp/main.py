optionPrompt = "Type add, edit, show or exit: "
option = ""

todoPrompt = "Enter a To-Do: "
todo = ""

numPrompt = "Which To-Do do you want to edit? "
num = 0

todos = []

while True:
    option = input(optionPrompt).lower().strip()
    match option:
        case "add":
            todo = input(todoPrompt).capitalize().strip()
            todos.append(todo)
        case "edit":
            num = int(input(numPrompt)) - 1
            todo = input(todoPrompt).capitalize().strip()
            todos[num] = todo
        case "show":
            for i, item in enumerate(todos, start=1):
                print(f"{i}. {item}")
        case "exit":
            break
        case _:
            print("Wrong input, try again.")

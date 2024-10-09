todo = ""
todoPrompt = "Enter a To-Do: "

todos = []

option = ""
optionPrompt = "Type add, edit, show, complete or exit: "

num = 0
numPrompt = "Got it. Which one? "

row = ""

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

prompt = "Enter To-Do: "
todo = ""
todos = []

while True:
    todo = input(prompt)
    todo = todo.title()
    todos.append(todo)
    print(todos)

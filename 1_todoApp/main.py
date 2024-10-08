prompt = "Enter To-Do: "
todo = ""
todos = []

while True:
    todo = input(prompt)
    todo = todo.capitalize()
    todos.append(todo)
    print(todos)

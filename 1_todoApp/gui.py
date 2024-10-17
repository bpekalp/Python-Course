import func.readWrite as rw
import func.textFormatter as tf
import func.stringToNum as stn
import func.dateTimeFormatter as dtf
import FreeSimpleGUI as sg

todos = []

filePath = "data/.todos.txt"

title = "Coolest To-Do App Ever!"

today = sg.Text(key="kToday", text=dtf.formatDateTime())

labelTodoText = sg.Text(key="kLabelTodo", text="Enter a To-Do")
todoText = sg.InputText(key="kTodo", tooltip="Here goes your To-Do!")

labelTodosList = sg.Text(key="kLabelTodos")
todosList = sg.Listbox(
    key="kTodos", values=rw.readTodos(filePath), enable_events=True, size=(36, 12)
)

addButton = sg.Button(key="kAdd", button_text="Add")
editButton = sg.Button(key="kEdit", button_text="Edit")
completeButton = sg.Button(key="kComplete", button_text="Complete")
exitButton = sg.Button(key="kExit", button_text="Exit Program")

layout = [
    [today],
    [labelTodoText],
    [todoText, addButton],
    [labelTodosList],
    [todosList, editButton, completeButton],
    [exitButton],
]


def main():
    window = sg.Window(title=title, layout=layout, font=("Segoe UI", 12))
    while True:
        event, value = window.read()
        print(f"Event: {event}")
        print(f"Todo List Value: {value["kTodos"]}")
        print(f"All the Values: {value}")

        match event:
            case "kTodos":
                todo = value["kTodos"][0]
                window["kTodo"].update(value=todo)

            case "kAdd":
                todos = rw.readTodos(filePath)

                todo = tf.textBoxToTodo(value, "kTodo")
                todos.append(todo)

                rw.writeTodos(todos, filePath)

                window["kTodos"].update(values=todos)

            case "kEdit":
                todos = rw.readTodos(filePath)

                todo = tf.textBoxToTodo(value, "kTodo")
                tempTodo = value["kTodos"][0]
                index = todos.index(tempTodo)
                todos[index] = todo

                rw.writeTodos(todos)

                window["kTodos"].update(values=todos)

            case "kComplete":
                print()

            case "kExit":
                break

            case sg.WIN_CLOSED:
                break

    window.close()


if __name__ == "__main__":
    main()

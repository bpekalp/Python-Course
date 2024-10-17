import func.readWrite as rw
import func.stringToNum as stn
import func.dateTimeFormatter as dtf
import FreeSimpleGUI as sg

todos = []

filePath = "data/.todos.txt"

title = "Coolest To-Do App Ever!"

today = sg.Text(key="kToday", text=dtf.formatDateTime())

labelToDoText = sg.Text(key="kLabelToDo", text="Enter a To-Do")
toDoText = sg.InputText(key="kToDo", tooltip="Here goes your To-Do!")

addButton = sg.Button(key="kAdd", button_text="Add")

layout = [[today], [labelToDoText], [toDoText, addButton]]


def main():
    window = sg.Window(title=title, layout=layout, font=("Segoe UI", 12))
    while True:
        event, value = window.read()
        print(event, value)

        match event:
            case "kAdd":
                todos = rw.readTodos(filePath)

                todo = value["kToDo"] + "\n"
                todos.append(todo)

                rw.writeTodos(todos, filePath)

            case sg.WIN_CLOSED:
                break

    window.close()


if __name__ == "__main__":
    main()

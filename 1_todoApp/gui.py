import func.readWrite as rw
import func.textFormatter as tf
import func.updateWindow as uw
import func.stringToNum as stn
import func.dateTimeFormatter as dtf
import FreeSimpleGUI as sg

todos = []

filePath = "data/.todos.txt"

title = "Coolest To-Do App Ever!"

labelToday = sg.Text(key="lbl_Today", text=dtf.formatDateTime())

labelTodoText = sg.Text(key="lbl_Todo", text="Enter a To-Do")
todoText = sg.InputText(key="tb_Todo", tooltip="Here goes your To-Do!")

labelTodosList = sg.Text(key="lbl_Todos")
todosList = sg.Listbox(
    key="listBox_Todos",
    values=rw.readTodos(filePath),
    enable_events=True,
    size=(36, 12),
)

addButton = sg.Button(key="btn_Add", button_text="Add")
editButton = sg.Button(key="btn_Edit", button_text="Edit")
completeButton = sg.Button(key="btn_Complete", button_text="Complete")
exitButton = sg.Button(key="btn_Exit", button_text="Exit Program")

layout = [
    [labelToday],
    [labelTodoText],
    [todoText, addButton],
    [labelTodosList],
    [todosList, editButton, completeButton],
    [exitButton],
]


def main():
    window = sg.Window(title=title, layout=layout, font=("Segoe UI", 12))
    while True:
        eventName, values = window.read()
        print(f"Event Name (key=): {eventName}")
        print(f"Todo List Value (values[key]): {values["listBox_Todos"]}")
        print(f"All the Values (values): {values}")
        print()

        match eventName:
            case "listBox_Todos":
                todo = str(values["listBox_Todos"][0]).strip("\n")

                uw.updateTodoBox(window, "tb_Todo", todo)

            case "btn_Add":
                todos = rw.readTodos(filePath)

                todo = tf.textBoxToTodo(values, "tb_Todo")
                todos.append(todo)

                rw.writeTodos(todos, filePath)

                uw.updateTodoList(window, "listBox_Todos", todos)

            case "btn_Edit":
                todos = rw.readTodos(filePath)

                todo = tf.textBoxToTodo(values, "tb_Todo")
                tempTodo = values["listBox_Todos"][0]
                index = todos.index(tempTodo)
                todos[index] = todo

                rw.writeTodos(todos)

                uw.updateTodoList(window, "listBox_Todos", todos)

            case "btn_Complete":
                print()

            case "btn_Exit":
                break

            case sg.WIN_CLOSED:
                break

    window.close()


if __name__ == "__main__":
    main()

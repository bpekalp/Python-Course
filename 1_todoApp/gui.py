import func.readWrite as rw
import func.textFormatter as tf
import func.windowUpdater as wu
import func.indexer as ir
import func.dateTimeFormatter as dtf
import FreeSimpleGUI as sg

todos = []
filePath = "data/.todos.txt"

title = "Coolest To-Do App Ever!"

today = dtf.formatDateTime()
labelToday = sg.Text(key="lbl_Today", text=today)

labelTodoText = sg.Text(key="lbl_Todo", text="Enter a To-Do")
todoText = sg.InputText(key="tb_Todo", tooltip="Here goes your To-Do!")

labelTodosList = sg.Text(key="lbl_Todos")
todosList = sg.Listbox(
    key="listBox_Todos",
    values=rw.readTodos(filePath),
    enable_events=True,
    size=(60, 15),
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
        eventName, values = window.read(timeout=1000)

        today = dtf.formatDateTime()
        wu.updateWindow(window, "lbl_Today", "text", today)
        print(f"Event Name (key=): {eventName}")
        print(f"All the Values (values): {values}")
        print()

        if eventName in (None, sg.WIN_CLOSED, "btn_Exit"):
            break

        match eventName:
            case "listBox_Todos":
                try:
                    todo = str(values["listBox_Todos"][0]).strip("\n")
                    wu.updateWindow(window, "tb_Todo", "text", todo)

                except IndexError:
                    popup = sg.popup_ok(
                        "Please add or select a To-Do first.",
                        title="Oops!",
                        font=("Segoe UI", 12),
                    )

            case "btn_Add":
                todos = rw.readTodos(filePath)

                todo = tf.textBoxToTodo(values, "tb_Todo")
                todos.append(todo)

                rw.writeTodos(todos, filePath)
                wu.updateWindow(window, "listBox_Todos", "list", todos)

            case "btn_Edit":
                try:
                    todos = rw.readTodos(filePath)

                    todo = tf.textBoxToTodo(values, "tb_Todo")
                    index = ir.getTodoIndex(values, "listBox_Todos", todos)
                    todos[index] = todo

                    rw.writeTodos(todos)
                    wu.updateWindow(window, "listBox_Todos", "list", todos)

                except IndexError:
                    popup = sg.popup_ok(
                        "Please add or select a To-Do first.",
                        title="Oops!",
                        font=("Segoe UI", 12),
                    )

            case "btn_Complete":
                try:
                    todos = rw.readTodos(filePath)

                    index = ir.getTodoIndex(values, "listBox_Todos", todos)
                    popped = todos.pop(index).strip("\n")

                    rw.writeTodos(todos)
                    wu.updateWindow(window, "listBox_Todos", "list", todos)
                    wu.updateWindow(window, "tb_Todo", "text", "")
                except IndexError:
                    popup = sg.popup_ok(
                        "Please add or select a To-Do first.",
                        title="Oops!",
                        font=("Segoe UI", 12),
                    )

    window.close()


if __name__ == "__main__":
    main()

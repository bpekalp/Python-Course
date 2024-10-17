import func.readWrite as rw
import func.stringToNum as stn
import func.dateTimeFormatter as dtf
import FreeSimpleGUI as gui

title = "Coolest To-Do App Ever!"

today = gui.Text(dtf.formatDateTime())

labelTextBox = gui.Text("Enter a To-Do")
textBox = gui.InputText(tooltip="Here goes your To-Do!")

addButton = gui.Button("Add")

layout = [[today], [labelTextBox], [textBox, addButton]]


def main():
    window = gui.Window(title=title, layout=layout)
    window.read()
    window.close()


if __name__ == "__main__":
    main()

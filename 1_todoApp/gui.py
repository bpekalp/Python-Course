import func.readWrite as rw
import func.stringToNum as stn
import func.dateTimeFormatter as dtf
import FreeSimpleGUI as sg

title = "Coolest To-Do App Ever!"

today = sg.Text(dtf.formatDateTime())

labelTextBox = sg.Text("Enter a To-Do")
textBox = sg.InputText(tooltip="Here goes your To-Do!")

addButton = sg.Button("Add")

layout = [[today], [labelTextBox], [textBox, addButton]]


def main():
    window = sg.Window(title=title, layout=layout)
    window.read()
    window.close()


if __name__ == "__main__":
    main()

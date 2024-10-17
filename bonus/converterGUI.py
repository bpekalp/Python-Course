import FreeSimpleGUI as sg

feetLabel = sg.Text("Enter feet:")
feetTextBox = sg.Input()

inchesLabel = sg.Text("Enter inches:")
inchesTextBox = sg.Input()

convertButton = sg.Button("Convert")

layout = [[feetLabel, feetTextBox], [inchesLabel, inchesTextBox], [convertButton]]

window = sg.Window(title="Feet Inches to Centimeters Conversion", layout=layout)
window.read()
window.close()

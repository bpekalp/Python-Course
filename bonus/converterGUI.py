import FreeSimpleGUI as sg
import func.converter as converter

feetLabel = sg.Text(key="lbl_Feet", text="Enter feet:")
feetTextBox = sg.Input(key="tb_Feet")

inchesLabel = sg.Text(key="lbl_Inches", text="Enter inches:")
inchesTextBox = sg.Input(key="tb_Inches")

convertButton = sg.Button(key="btn_Convert", button_text="Convert")
exitButton = sg.Button(key="btn_Exit", button_text="Exit")

outputLabel = sg.Text(key="lbl_Output")

layout = [
    [feetLabel, feetTextBox],
    [inchesLabel, inchesTextBox],
    [convertButton, exitButton, outputLabel],
]

window = sg.Window(title="Feet Inches to Centimeters Conversion", layout=layout)
while True:
    eventName, values = window.read()
    print(f"Event Name (key=): {eventName}")
    print(f"All the Values (values): {values}")
    print()

    if eventName in (None, sg.WIN_CLOSED, "btn_Exit"):
        break

    if eventName == "btn_Convert":
        try:
            feet = float(values["tb_Feet"])
            inches = float(values["tb_Inches"])

            cm = converter.convertToCm(feet, inches)

            output = f"{feet:.0f}'{inches:.0f} is equal to {cm:.2f} centimeters."

            window["lbl_Output"].update(value=output)
        except ValueError:
            popup = sg.popup_ok("Please type in a number.", title="Oops!")

window.close()

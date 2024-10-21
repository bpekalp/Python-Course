import FreeSimpleGUI as sg
import func.decompress as decompress

zipLabel = sg.Text(key="lbl_Zip", text="Select .zip file")
zipText = sg.Input(key="tb_Zip")
zipButton = sg.FileBrowse(key="btn_Zip", button_text="Browse File")

targetLabel = sg.Text(key="lbl_Target", text="Select target folder")
targetText = sg.Input(key="tb_Target")
targetButton = sg.FolderBrowse(key="btn_Target", button_text="Browse Folder")

decompressButton = sg.Button(key="btn_Decompress", button_text="Decompress!")
exitButton = sg.Button(key="btn_Exit", button_text="Exit")

outputLabel = sg.Text(key="lbl_Output", text="")

layout = [
    [zipLabel, zipText, zipButton],
    [targetLabel, targetText, targetButton],
    [decompressButton, exitButton, outputLabel],
]


def main():
    window = sg.Window(title="Best File Extractor!", layout=layout)
    while True:
        eventName, values = window.read()

        if eventName in (None, sg.WIN_CLOSED, "btn_Exit"):
            break

        elif eventName == "btn_Decompress":
            try:
                file = str(values["tb_Zip"])
                target = str(values["tb_Target"])
                status = decompress.fromZip(file, target)

                window["lbl_Output"].update(value=status)
            except FileNotFoundError:
                popup = sg.popup_ok(
                    "Please select file(s) first.", title="Error: File not found!"
                )

    window.close()


if __name__ == "__main__":
    main()

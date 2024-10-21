import FreeSimpleGUI as sg
import func.compress as compress

filesTextLabel = sg.Text(key="lbl_Files", text="Select files to compress")
filesText = sg.Input(key="tb_Files")
filesButton = sg.FilesBrowse(key="btn_Files", button_text="Browse Files")

zipTextLabel = sg.Text(key="lbl_Target", text="Select destination for .zip file")
zipText = sg.Input(key="tb_Target")
zipButton = sg.FolderBrowse(key="btn_Target", button_text="Browse Folder")

compressButton = sg.Button(key="btn_Compress", button_text="Compress!")
exitButton = sg.Button(key="btn_Exit", button_text="Exit")

outputLabel = sg.Text(key="lbl_Output")

layout = [
    [filesTextLabel, filesText, filesButton],
    [zipTextLabel, zipText, zipButton],
    [compressButton, exitButton, outputLabel],
]


def main():
    window = sg.Window(title="Best compresser!", layout=layout)
    while True:
        eventName, values = window.read()
        print(f"Event Name (key=): {eventName}")
        print(f"All the Values (values): {values}")
        print()

        files = str(values["tb_Files"]).split(";")
        target = str(values["tb_Target"])

        if eventName in (None, sg.WIN_CLOSED, "btn_Exit"):
            break

        if eventName == "btn_Compress":
            try:
                status = compress.toZip(files, target)
                window["lbl_Output"].update(value=status)

            except FileNotFoundError:
                popup = sg.popup_ok(
                    "Please select file(s) first.", title="Error: File not found!"
                )


if __name__ == "__main__":
    main()

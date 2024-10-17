import FreeSimpleGUI as sg

filesTextLabel = sg.Text("Select files to compress")
filesText = sg.Input()
filesButton = sg.FilesBrowse("Browse Files")

zipTextLabel = sg.Text("Select destination for .zip file")
zipText = sg.Input()
zipButton = sg.FolderBrowse("Browse Folder")

compressButton = sg.Button("Compress!")
exitButton = sg.Button("Exit")

layout = [
    [filesTextLabel, filesText, filesButton],
    [zipTextLabel, zipText, zipButton],
    [compressButton, exitButton],
]


def main():
    window = sg.Window(title="Best compresser!", layout=layout)
    window.read()
    window.close()


if __name__ == "__main__":
    main()

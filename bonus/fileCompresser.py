import FreeSimpleGUI as gui

filesTextLabel = gui.Text("Select files to compress")
filesText = gui.Input()
filesButton = gui.FilesBrowse("Browse Files")

zipTextLabel = gui.Text("Select destination for .zip file")
zipText = gui.Input()
zipButton = gui.FolderBrowse("Browse Folder")

layout = [[filesTextLabel, filesText, filesButton], [zipTextLabel, zipText, zipButton]]


def main():
    window = gui.Window(title="Best compresser!", layout=layout)
    window.read()
    window.close()


if __name__ == "__main__":
    main()

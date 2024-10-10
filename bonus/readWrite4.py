fileNames = ["doc.txt", "report.txt", "presentation.txt"]
filePath = "bonus/files"

for fileName in fileNames:
    file = open(f"{filePath}/{fileName}", "r")
    row = file.read()
    print(row)

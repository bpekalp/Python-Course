fileNames = ["doc.txt", "report.txt", "presentation.txt"]
filePath = "bonus/files"

for fileName in fileNames:
    file = open(f"{filePath}/{fileName}", "w")
    file.write(f"Hello {fileName}!")
    file.close()

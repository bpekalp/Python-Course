fileNames = ["1.doc", "2.report", "3.presentation"]

fileNames = [fileName.replace(".", "-") + ".txt" for fileName in fileNames]

for fileName in fileNames:
    print(fileName)

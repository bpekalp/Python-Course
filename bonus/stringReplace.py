fileNames = ["1.Stuff.txt", "2.School.txt", "3.Games.txt"]

for fileName in fileNames:
    fileName = fileName.replace(".", "-", 1)
    print(fileName)

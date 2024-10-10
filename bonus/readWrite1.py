contents = [
    "Goes into the A",
    "Goes into the B",
    "Goes into the C",
]

files = [".a.txt", ".b.txt", ".c.txt"]

for content, fileName in zip(contents, files):
    file = open(f"bonus/files/{fileName}", "w")
    file.write(content)
    file.close()

for fileName in files:
    file = open(f"bonus/files/{fileName}", "r")
    content = file.read()
    print(content)
    file.close()

filePath = "bonus/files/.members.txt"
optionPrompt = "Add, show, exit: "
memberPrompt = "Add a member: "

members = []

while True:
    option = input(optionPrompt).lower().strip()
    match option:
        case "add":
            file = open(filePath, "r")
            members = file.readlines()
            file.close()

            member = input(memberPrompt).title().strip() + "\n"
            members.append(member)

            file = open(filePath, "w")
            file.writelines(members)
            file.close()
        case "show":
            file = open(filePath, "r")
            rows = file.readlines()
            for i, row in enumerate(rows, start=1):
                output = f"{i}. {row}"
                print(output)
        case "exit":
            break

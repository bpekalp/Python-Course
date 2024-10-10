datePrompt = "Enter a date: "
moodPrompt = "How are you feeling today from 1 to 5? "
journalPrompt = "Write your thoughts..." + "\n"
journalPath = "bonus/files"

date = input(datePrompt)
mood = int(input(moodPrompt))
journal = input(journalPrompt)

journalFile = f"{journalPath}/{date}.txt"

match mood:
    case 1:
        moodRow = "I am feeling very bad today." + "\n"
    case 2:
        moodRow = "I am feeling bad today." + "\n"
    case 3:
        moodRow = "I am feeling normal today." + "\n"
    case 4:
        moodRow = "I am feeling good today!" + "\n"
    case 5:
        moodRow = "I am feeling very good today!" + "\n"
    case _:
        moodRow = "I don't know how I'm feeling today." + "\n"

with open(journalFile, "w") as file:
    file.write(moodRow + journal)

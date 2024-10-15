def parsing(length):
    length = length.split("'")
    feet, inches = float(length[0]), float(length[1])
    return feet, inches


def convertToCm(feet, inches):

    cm = feet * 30.48 + inches * 2.54
    return cm


while True:
    option = input("Type enter or exit: ")

    match option:
        case "enter":
            try:
                length = input("Enter feet and inches e.g 5'7: ")

                feet, inches = parsing(length)
                cm = convertToCm(feet, inches)

                print(f"{feet:.0f}'{inches:.0f} is {cm:.2f}cm.")
            except ValueError:
                print("Wrong input. Try again.")

        case "exit":
            print("Goodbye!")
            break

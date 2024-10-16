import parser
import converter

while True:
    option = input("Type enter or exit: ")

    match option:
        case "enter":
            try:
                length = input("Enter feet and inches e.g 5'7: ")

                feet, inches = parser.parse(length)
                cm = converter.convertToCm(feet, inches)

                print(f"{feet:.0f}'{inches:.0f} is {cm:.2f}cm.")
            except ValueError:
                print("Wrong input. Try again.")

        case "exit":
            print("Goodbye!")
            break

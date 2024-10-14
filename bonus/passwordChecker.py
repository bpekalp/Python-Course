upperCase = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowerCase = "qwertyuıopasdfghjklzxcvbnm"
numbers = "1234567890"
special = r"!'^+%&/()=?_,.<>£#$½{[]}\|;:>"

while True:

    option = input("Type enter or exit: ")

    match option:
        case "enter":
            password = input("Enter your password: ")
            strength = 0

            if len(password) > 8:
                strength += 5

            for letter in upperCase:
                if letter in password:
                    strength += 5
                    break

            for letter in lowerCase:
                if letter in password:
                    strength += 5
                    break

            for number in numbers:
                if number in password:
                    strength += 5
                    break

            for character in special:
                if character in password:
                    strength += 5
                    break

            print(strength)

            if strength <= 10:
                print("Your password is very weak.")

            elif strength <= 15:
                print("Your password is weak.")

            elif strength <= 20:
                print("Your password is strong!")

            else:
                print("Your password is very strong!")

        case "exit":
            break

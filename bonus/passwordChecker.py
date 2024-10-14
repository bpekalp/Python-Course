import string

while True:

    option = input("Type enter or exit: ")

    match option:
        case "enter":
            password = input("Enter your password: ")
            strength = 0

            if len(password) > 8:
                strength += 5

            for character in password:
                if character.isupper():
                    strength += 5
                    break

            for character in password:
                if character.islower():
                    strength += 5
                    break

            for character in password:
                if character.isnumeric():
                    strength += 5
                    break

            for character in password:
                if character in string.punctuation:
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

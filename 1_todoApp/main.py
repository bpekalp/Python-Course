# from readWrite import readTodos, writeTodos
# from stringToNum import stringToNum

import readWrite
import stringToNum

todos = []

todoPrompt = "Enter a To-Do: "
optionPrompt = (
    "Usage: add <To-Do>, edit <To-Do number>, show, complete <To-Do number> or exit: "
)
numPrompt = "Got it. Which one? "

filePath = "data/.todos.txt"


def main():
    while True:
        option = input(optionPrompt).lower().strip()

        if option.startswith("add"):
            todos = readWrite.readTodos(filePath)

            userIf = "add"
            todo = option.lstrip(userIf).strip().capitalize() + "\n"
            todos.append(todo)

            readWrite.writeTodos(todos, filePath)

        elif option.startswith("edit"):
            try:
                todos = readWrite.readTodos(filePath)

                userIf = "edit"
                num = stringToNum.stringToNum(option, userIf)

                todo = input(todoPrompt).strip().capitalize() + "\n"
                todos[num] = todo

                readWrite.writeTodos(todos, filePath)

            except ValueError:
                message = "Usage: edit <To-Do number to edit>"
                print(message)
                continue

            except IndexError:
                message = "The number was out of bounds of the To-Do list."
                print(message)
                continue

        elif option.startswith("show"):
            todos = readWrite.readTodos(filePath)

            # todos = [todo.strip("\n") for todo in todos]
            for i, todo in enumerate(todos, start=1):
                todo = todo.strip("\n")
                message = f"{i}. {todo}"
                print(message)

        elif option.startswith("complete"):
            try:
                todos = readWrite.readTodos(filePath)

                userIf = "complete"
                num = stringToNum.stringToNum(option, userIf)

                todo = todos.pop(num).strip("\n")
                message = f"{todo} is marked as done and removed from the list."
                print(message)

                readWrite.writeTodos(todos, filePath)

            except ValueError:
                message = "Usage: complete <To-Do number to complete>"
                print(message)
                continue

            except IndexError:
                message = "The number was out of bounds of the To-Do list."
                print(message)
                continue

        elif option.startswith("exit"):
            message = "Goodbye!"
            print(message)
            break

        else:
            message = "Wrong input, try again."
            print(message)


if __name__ == "__main__":
    main()

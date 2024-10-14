def averageOf(numbers):
    try:
        result = sum(numbers) / len(numbers)
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0


with open("bonus/files/.numbers.txt") as file:
    numbers = file.readlines()

try:
    numbers = [float(number) for number in numbers]
    average = averageOf(numbers)

    print(average)

except ValueError:
    print("The file contains non numeric values.")

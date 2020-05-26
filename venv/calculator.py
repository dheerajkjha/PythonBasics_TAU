"""

def addition():
    num_one = float(input("Please enter a number. "))
    num_two = float(input("Please enter another number. "))
    print(num_one + num_two)


def substratction():
    num_one = float(input("Please enter a number. "))
    num_two = float(input("Please enter another number. "))
    print(num_one - num_two)


def multiplication():
    num_one = float(input("Please enter a number. "))
    num_two = float(input("Please enter another number. "))
    print(num_one * num_two)


def division():
    num_one = float(input("Please enter a number. "))
    num_two = float(input("Please enter another number. "))
    print(num_one / num_two)


operation = input("Please type +, -, * or / ")

if operation == "+":
    addition()
elif operation == "-":
    substratction()
elif operation == "*":
    multiplication()
elif operation == "/":
    division()
else:
    print("Your selection is incorrect.")

"""

num_one = float(input("Enter first number. "))
num_two = float(input("Enter another number. "))
operation = input("Please type the opration you want to perform +, -, * or / ")


def addition(num_one, num_two):
    print(num_one + num_two)


def substraction(num_one, num_two):
    print(num_one - num_two)


def multiplication(num_one, num_two):
    print(num_one * num_two)

def division(num_one, num_two):
    print(num_one / num_two)

if operation == "+":
    addition(num_one, num_two)
elif operation == "-":
    substraction(num_one, num_two)
elif operation == "*":
    multiplication(num_one, num_two)
elif operation == "/":
    division(num_one, num_two)
else:
    print("Incorrect operation. ")

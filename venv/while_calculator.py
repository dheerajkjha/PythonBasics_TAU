on = True

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

while on:
    operation = input("Please type +, -, *, / or q ")
    if operation == "+":
        addition()
    elif operation == "-":
        substratction()
    elif operation == "*":
        multiplication()
    elif operation == "/":
        division()
    elif operation == "q":
        on = False
    else:
        print("Your selection is incorrect.")
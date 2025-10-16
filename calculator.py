import time


def start():
    print("╔══════════════════════════════╗")
    print("║           CALCULATOR         ║")
    print("╚══════════════════════════════╝")
def line():
    print("________________________________________")

start()

while True:
    choice = str(input("Do you want to continue? (y/n/m) > ")).lower()

    if choice == "n":
        print("Goodbye!")
        break

    elif choice == "y":
        print("Continuing...")
        line()
        time.sleep(2.5)

    elif choice == "m":
        print("+ = Addition\n- = Subtraction\n* = Multiplication\n/ = Division\n// = Square root\n** = Power")
        print("NOTE: If it’s a square root, you don’t need to add the second number.")
        line()
        exit()

    else:
        print("Invalid format!")
        exit()

    operation = input("Enter the operation: \n+\n-\n/\n**\n//\n> ").lower()
    line()
    try:
        num1 = float(input("Enter the first number: "))
        line()
        if operation != "//":
            num2 = float(input("Enter the second number: "))
        line()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            if num2 == 0:
                print("ERROR: Division by 0")
            else:
                result = num1 / num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "**":
            result = num1 ** num2
        elif operation == "//":
            result = num1 ** 0.5
        else:
            print("Corrupted result!")
            result = "Invalid symbol!"

    except ValueError:
        result = "Invalid symbol!"


    if result == "Invalid symbol!":
        print("Invalid result.")
    else:
        print(f"The result is {result}")
    print("__________________________________")


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 and num1 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero!"

def modulus(num1, num2):
    return num1 % num2

def expo(num1 , num2):
    return (num1 ** num2)

def calculator():
    userName = input("Enter your name: ")  # user input as name 
    print(f"Hello, {userName}!")
    print("Welcome to this simple calculator where you can perform arithmetic operations.")

    while True:  # loop for the calculator run again and again without running code everytime until user enter 7 for exit 
        try:
            num1 = float(input("Enter the first number: "))    # first number for input 
            num2 = float(input("Enter the second number: "))   # second number for input 
        except: 
            print("Error: Invalid input, please input number only.")  #error if user inputs anything other then numbers 
            continue

                    

        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponent")
        print("7. Exit")

        operation = input("Enter your choice: ")

        if operation == "1":
            result = add(num1, num2)
            print("Result:", result)
        elif operation == "2":
            result = subtract(num1, num2)
            print("Result:", result)
        elif operation == "3":
            result = multiply(num1, num2)
            print("Result:", result)
        elif operation == "4":
            result = divide(num1, num2)
            print("Result:", result)
        elif operation == "5":
            result = modulus(num1, num2)
            print("Result:", result)
        elif operation == "6": 
            result = expo(num1 , num2)
            print(f"Result: {result}")
        elif operation == "7":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid operation.")

calculator()  # calling the function 
 
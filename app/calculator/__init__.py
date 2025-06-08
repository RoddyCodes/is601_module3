from app.operations import Operations

def calculator():
    # First, we print a message to welcome the user to the calculator.
    print("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break
        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)

        except ValueError:
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue

        # Now we check what operation the user asked for and call the right function (addition, subtraction, etc.).
        if operation == "add":
            result = Operations.addition(num1, num2)  # We call the addition function to add the two numbers.
        elif operation == "subtract":
            result = Operations.subtraction(num1, num2)  # We call the subtraction function to subtract the two numbers.
        elif operation == "multiply":
            result = Operations.multiplication(num1, num2)  # We call the multiplication function to multiply the two numbers.
        elif operation == "divide":
            try:
                result = Operations.division(num1, num2)  # We call the division function to divide the two numbers.
            except ValueError as e:
                print(e)  # Show the error message.
                continue  
        else:
            # If the user types an operation we don't understand, we show them a message.
            print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
            continue  # Go back to the top of the loop and try again.

        # Finally, we print the result of the operation (for example, "Result: 8").
        print(f"Result: {result}")
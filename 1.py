import math

def calculator():
    print("Advanced Calculator")
    print("Enter 'exit' to quit")

    while True:
        expression = input("Enter expression: ")

        if expression.lower() == 'exit':
            print("Exiting calculator...")
            break

        try:
            # Evaluate the expression
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()


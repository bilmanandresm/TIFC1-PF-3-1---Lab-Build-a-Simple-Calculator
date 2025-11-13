"""num1 =int (input("Ingresa el primer numero: "))
num2 =int (input("Ingresa el segundo numero: "))

resul = num1 + num2

print("El resultado es:", resul) 
"""
# Simple Calculator - Main Task
# First, the program must ONLY add two numbers for the automatic grader

num1 = float(input())
num2 = float(input())

result = num1 + num2
print(result)

# ------------------------------
# EXTRA FEATURES (manual grading)
# ------------------------------

print("\nExtra features menu:")
print("1. Subtract two numbers")
print("2. Multiply two numbers")
print("3. Divide two numbers")
print("4. Modulus of two numbers")
print("5. Choose operation (+, -, *, /, %)")
print("6. Add 3 numbers")
print("7. Mixed operations (expression)")

choice = input("Choose an option: ")

# 1. Subtraction
if choice == "1":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a - b)

# 2. Multiplication
elif choice == "2":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)

# 3. Division
elif choice == "3":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)

# 4. Modulus
elif choice == "4":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a % b)

# 5. User chooses operator
elif choice == "5":
    a = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /, %): ")
    b = float(input("Enter second number: "))

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)
    elif op == "%":
        print("Result:", a % b)
    else:
        print("Invalid operator")

# 6. Add 3 numbers
elif choice == "6":
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    c = float(input("Enter number 3: "))
    print("Result:", a + b + c)

# 7. Mixed operations (expression)
elif choice == "7":
    expr = input("Enter an expression (example: 2 + 4 - 3): ")
    try:
        print("Result:", eval(expr))
    except:
        print("Invalid expression")

else:
    print("Invalid choice")

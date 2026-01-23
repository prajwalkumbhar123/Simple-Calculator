# 🧮 Simple Calculator in Python

This is a basic **command-line calculator** built using Python.  
It allows users to perform common arithmetic operations on two numbers.

## 🚀 Features

- Addition
- Subtraction
- Multiplication
- Division
- Average calculation
- User-friendly menu-driven interface

## 🛠️ Technologies Used

- Python 3

## 📌 How It Works

1. The user enters two numbers.
2. The user selects an operation from the menu.
3. The program performs the chosen calculation.
4. The result is displayed on the screen.

## 📄 Source Code

```python
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter Which Operation You Want To Perform:\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Average")

choice = int(input("Enter Your Choice (1-5): "))

if choice == 1:
    print("Addition =", num1 + num2)
elif choice == 2:
    print("Subtraction =", num1 - num2)
elif choice == 3:
    print("Multiplication =", num1 * num2)
elif choice == 4:
    print("Division =", num1 / num2)
elif choice == 5:
    print("Average =", (num1 + num2) / 2)
else:
    print("Invalid operation! Please try again.")

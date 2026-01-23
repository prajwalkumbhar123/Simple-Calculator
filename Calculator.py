# This is simple calculator

num1 =int(input("Enter First Number:"))
num2 =int(input("Enter First Number:"))

print("Enter Which Operation You Want To Perform: \n" \
"1. Addition\n"
"2. Subtraction\n"
"3. Multiplication\n"
"4. Division\n"
"5. Average")

choice=int(input("Enter Your Choice(1-5):"))


if choice == 1 :
    add= num1 + num2
    print("Addition of ", num1, "+", num2,"=", add )
     
elif choice == 2 :
    sub= num1 - num2
    print("Subtraction of ", num1, "-", num2,"=", sub )

elif choice == 3 :
    mul= num1 * num2
    print("Multiplication of ", num1, "*", num2,"=", mul )
     
elif choice == 4 :
    div= num1 / num2
    print("Division of ", num1, "/", num2,"=", div )

elif choice == 5 :
    div= (num1 + num2)/2
    print("Average of ", "(" ,num1, "+", num2,") /2 =", div )
    
else :
    print("Invalid operation! Pls select again!" )

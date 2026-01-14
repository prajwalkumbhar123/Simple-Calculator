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
     
elif select == 2:
     print(number1, "-", number2, "= ", \
           sub(number1, number2)) 
     
elif select == 3:
     print(number1, "*", number2, "= ", \
           multiply(number1, number2))
     
elif select == 4:
     print(number1, "/", number2, "= ", \
           divide(number1, number2))

elif select == 5:
     print("(",number1, "+", number2, ")", "/", "2", "= ", \
           avg(number1, number2)) 
    
else:
     print("Invalid operation! Pls select again!")
     




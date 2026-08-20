operator = input("Enter the operator: ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if operator == "+":
    print(f"The Addition of {num1} and  {num2} = ",num1 + num2)

elif operator == "-":
    print(f"The substraction of {num1} and {num2} = ",num1 - num2)

elif operator == "*":
    print(f"The Multiplication of {num1} and {num2} = ",num1 * num2)

elif operator == "/":
    print(f"The Division of {num1} and {num2} = ",num1 / num2)
            
else:
    print("Invlid Input pls enter the valid input")







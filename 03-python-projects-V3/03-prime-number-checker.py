
try:
    number = int(input("Enter The Number to check: "))
    prime = True

    if number <=1:
        print("Its Not a prime number")

    elif number >=1:
        for i in range(2,int(number**0.5)+1):
            if number % i == 0:
                prime = False
                break

    else:
        print("error")

    if prime == True:
        print(f"{number} is a prime number")

    elif prime == False:
        print(f"{number} is not a prime number")                            

except ValueError:
    print("invalid Input Enter Numbers to check prime or not.")
import random 

guess_no = random.randint(1,100)
#print(guess_no)

u_input = 0

while u_input != guess_no:
    u_input = int(input("Enter Your Quess: "))


    if u_input > guess_no:
        print("Guess Lower")

    elif u_input < guess_no:
        print("Guess Higher")
    elif u_input == guess_no:
        print()
        print("-" * 39)
        print(f"  The Number was '{guess_no}' You Won The Game!!")
        print("-" * 39)
        print()

    else:
        print()

        
    


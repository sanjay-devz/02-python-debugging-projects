number = int(input("Enter The Number to Get Multiplication: "))
row = int(input("Enter The Number of Rows needed: "))
for num in range(1, row + 1):
    print(f"{number} x {num} = {number * num}")
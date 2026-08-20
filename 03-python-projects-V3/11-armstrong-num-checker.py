number = int(input("Enter the number to check: "))

original = number
digits = len(str(number))
total = 0

while number > 0:
    digit = number % 10
    total += digit ** digits
    number = number // 10

if total == original:
    print(original,'is a armstrong number')
else:
    print(original,"is not a armstrong number")

    


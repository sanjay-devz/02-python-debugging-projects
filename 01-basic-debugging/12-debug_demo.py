def calculate_total(price, quantity):
    total = price * quantity
    return total


price = 150
quantity = 3

bill = calculate_total(price, quantity)

discount = 50

final_bill = bill - discount

print("Bill:", bill)
print("Final Bill:", final_bill)  
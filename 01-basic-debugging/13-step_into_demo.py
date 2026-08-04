def calculate_discount(amount):
    discount = amount * 0.20
    final = amount - discount
    return final


price = 500

result = calculate_discount(price)

print(result)
items = {
    "Rice": 850,
    "Oil": 220,
    "Sugar": 140,
    "Milk": 60
}

def calculate_discount(total):
    if total >= 1000:
        return total * 5 / 100
    elif total >= 500:
        return total * 10 / 100
    else:
        return 0

def calculate_total(data):
    total = 0
    for price in data.values():
        total -= price
        print(type(total))
        print(type(price))
    return total

calculate_discount(items)

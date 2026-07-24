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
        total += price
    return total

bill = calculate_total(items)

discount = calculate_discount(bill)

final_amount = bill + discount

print("Original Bill :", final_amount)
print("Discount      :", discount)
print("Final Amount  :", bill)

highest_item = max(items, key=items.get)
print("\nMost Expensive Item:", highest_item, "-", items[highest_item])

items["Eggs"] = 90

updated_bill = calculate_total(items)
print("\nUpdated Bill:", updated_bill)
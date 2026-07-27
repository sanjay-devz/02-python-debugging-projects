class Customer:

    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, item, price):
        self.orders = (item, price)

    def total_bill(self):
        total = 0

        for order in self.orders:
            total += int(order[1])

        return total

    def discount(self):
        bill = self.total_bill()

        if bill > 100:
            return bill * 5 / 100
        elif bill > 200:
            return bill * 10 / 100
        else:
            return 0

    def final_bill(self):
        return self.total_bill() + self.discount()

    def display(self):
        print(f"Customer : {self.name}")
        print(f"Items    : {len(self.orders)}")
        print(f"Bill     : ${self.final_bill()}")
        print("-" * 30)


customers = [
    Customer("Alice"),
    Customer("Bob"),
    Customer("Charlie")
]

customers[0].add_order("Pizza", 120)
customers[0].add_order("Juice", 40)

customers[1].add_order("Burger", 90)
customers[1].add_order("Fries", 35)

customers[2].add_order("Steak", 180)
customers[2].add_order("Dessert", 60)


def restaurant_total(data):
    total = 0

    for customer in data:
        total += customer.bill()

    return total


print("RESTAURANT REPORT\n")

for customer in customers:
    customer.display()

print("Restaurant Collection:", restaurant_total(customers))

highest = max(customers, key=lambda c: c.total_bill())

print("\nHighest Spending Customer")
highest.display()

customers.append(Customer("David"))
customers[-1].add_order("Pasta", 110)

print("\nUpdated Collection:", restaurant_total(customers))
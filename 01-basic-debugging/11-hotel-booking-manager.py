class Guest:

    def __init__(self, name):
        self.name = name
        self.bookings = []

    def add_booking(self, nights, price):
        self.bookings = (nights, price)

    def room_bill(self):
        total = 0
       
        for booking in self.bookings:
            total += booking[0] * booking[1]


        return total

    def discount(self):
        bill = self.room_bill()

        if bill > 500:
            return bill * 0.15
        elif bill > 250:
            return bill * 0.1
        else:
            return 0

    def final_bill(self):
        return self.room_bill() - self.discount()

    def display(self):
        print(f"Guest    : {self.name}")
        print(f"Bookings : {len(self.bookings)}")
        print(f"Bill     : £{self.final_bill()}")
        print("-" * 30)


guests = [
    Guest("Alice"),
    Guest("Bob"),
    Guest("Charlie")
]

guests[0].add_booking(3, 120)
guests[0].add_booking(2, 150)

guests[1].add_booking(2, 90)
guests[1].add_booking(1, 80)

guests[2].add_booking(4, 180)
guests[2].add_booking(2, 160)


def hotel_revenue(data):
    total = 0

    for guest in data:
        total += guest.bill()

    return total


print("HOTEL BOOKING REPORT\n")

for guest in guests:
    guest.display()

print("Hotel Revenue:", hotel_revenue(guests))

highest = max(guests, key=lambda g: g.final_bill())

print("\nHighest Paying Guest")
highest.display()

guests.append(Guest("David"))
guests[3].add_booking(2, 200)

print("\nUpdated Revenue:", hotel_revenue(guests))

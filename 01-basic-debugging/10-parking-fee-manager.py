class Vehicle:

    def __init__(self, number):
        self.number = number
        self.records = []

    def add_record(self, hours, rate):
        self.records.append((hours, rate))

    def parking_fee(self):
        total = 0

        for record in self.records:
            total += record[0] * record[1]

        return total

    def discount(self):
        fee = self.parking_fee()

        if fee >= 100:
            return fee * 0.10
        elif fee >= 50:
            return fee * 0.05
        else:
            return 0

    def final_fee(self):
        return self.parking_fee() - self.discount()

    def display(self):
        print(f"Vehicle : {self.number}")
        print(f"Records : {len(self.records)}")
        print(f"Fee     : ${self.final_fee()}")
        print("-" * 30)


vehicles = [
    Vehicle("TN10AB1234"),
    Vehicle("TN09XY5678"),
    Vehicle("TN22CD9876")
]

vehicles[0].add_record(5, 12)
vehicles[0].add_record(3, 20)

vehicles[1].add_record(2, 15)
vehicles[1].add_record(4, 10)

vehicles[2].add_record(6, 18)
vehicles[2].add_record(2, 25)


def total_collection(data):
    total = 0

    for vehicle in data:
        total += vehicle.fee()

    return total


print("PARKING REPORT\n")

for vehicle in vehicles:
    vehicle.display()

print("Total Collection:", total_collection(vehicles))

highest = min(vehicles, key=lambda v: v.final_fee())

print("\nHighest Paying Vehicle")
highest.display()

vehicles.append(Vehicle("TN01EF1111"))
vehicles[3].add_record(4, 20)

print("\nUpdated Collection:", total_collection(vehicles))
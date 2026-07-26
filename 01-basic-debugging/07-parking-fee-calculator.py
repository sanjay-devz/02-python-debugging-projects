vehicles = [
    ["TN01AB1234", 2],
    ["TN09XY4567", 5],
    ["TN22CD8901", 8],
    ["TN14EF1111", 1]
]
 
RATE_PER_HOUR = 30

def calculate_fee(hours):
    return hours * RATE_PER_HOUR

def parking_summary(data):
    total = 0

    for vehicle in data:
        number = vehicle[0]
        hours = vehicle[1]

        fee = calculate_fee(hours)

        print(f"Vehicle: {number}")
        print(f"Hours  : {hours}")
        print(f"Fee    : ₹{fee}")
        print("-" * 25)

        total += fee

    average = total // len(data)

    print("\nTotal Collection:", total)
    print("Average Fee:", average)

parking_summary(vehicles)

highest = max(vehicles, key=lambda x: calculate_fee(x[1]))

print("\nHighest Paying Vehicle:")
print(highest[0], "paid ₹", calculate_fee(highest[1]))

vehicles.append(["TN77ZZ9999", 4])

print("\nUpdated Summary")
parking_summary(vehicles)
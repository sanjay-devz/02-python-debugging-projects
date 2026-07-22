numbers = [12, 5, 8, 15, 20, 7]

def calculate_average(nums):
    total = 0
    for n in nums:
        total += n
    average = total / len(nums)
    return average

def find_even(nums):
    even = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
    return even

avg = calculate_average(numbers)
print("Average:", avg)

evens = find_even(numbers)
print("Even Numbers:", evens)

largest = max(numbers)
print("Largest Number:", largest)

print("Program Finished!")
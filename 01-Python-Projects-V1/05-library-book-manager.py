books = {
    "Python Basics": 450,
    "Data Science": 650,
    "Machine Learning": 900,
    "Algorithms": 700
}

borrowed = ["Python Basics", "Algorithms"]

def available_books(all_books, borrowed_books):
    available = []
    for book in all_books:
        if book not in borrowed_books:
            available.append(book)
    return available

def total_book_value(data):
    total = 0
    for price in data.values():
        total += price
    return total

available = available_books(books, borrowed)
print("Available Books:", available)

total = total_book_value(books)
print("Total Book Value:", total)

most_expensive = max(books, key=books.get)
print("Most Expensive Book:", most_expensive, "-", books[most_expensive])

average = total / (len(books))
print("Average Book Price:", average)

books["Networking"] = 550

print("\nUpdated Total Value:", total_book_value(books))

print("Library Updated Successfully!")
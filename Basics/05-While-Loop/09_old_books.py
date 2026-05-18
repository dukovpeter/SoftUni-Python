searched_book = input("")
checked_books = 0

while True:
    new_book = input("")
    if new_book != searched_book and new_book != "No More Books":
        checked_books += 1

    if new_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break

    if new_book == searched_book:
        print(f"You checked {checked_books} books and found it.")
        break
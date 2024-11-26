
book_borrowed_days = {}

def accept_books():
    print("Enter the books and days borrowed in the format: 'Book Title - Days Borrowed'")
    print("Type 'done' when you are finished.")
    
    while True:
        user_input = input("Enter book and borrowed days: ")
        if user_input.lower() == 'done':
            break
        
        if " - " in user_input:
            book_title, borrowed_days = user_input.split(" - ")
            
            # Remove any leading/trailing whitespace from book title and borrowed days
            book_title = book_title.strip()
            borrowed_days = borrowed_days.strip()
            
            # Convert borrowed days to integer
            try:
                borrowed_days = int(borrowed_days)
                # Store or update the dictionary
                if book_title in book_borrowed_days:
                    book_borrowed_days[book_title] += borrowed_days  # Update the borrowed days if the book already exists
                else:
                    book_borrowed_days[book_title] = borrowed_days  # Add new book with borrowed days
            except ValueError:
                print("Error: Please enter the days as a number.")
        else:
            print("Invalid format! Please use 'Book Title - Days Borrowed'.")
    
    print("\nFinal list of books and borrowed days:")
    for title, days in book_borrowed_days.items():
        print(f"'{title}' - {days} days")
    
    if book_borrowed_days:
        most_borrowed_book = max(book_borrowed_days, key=book_borrowed_days.get)
        least_borrowed_book = min(book_borrowed_days, key=book_borrowed_days.get)
        #.get()  is used as the key function, which returns the value (borrowed days) for each book.
        # Print the most and least borrowed books
        print(f"\nMost Borrowed Book: '{most_borrowed_book}' with {book_borrowed_days[most_borrowed_book]} days.")
        print(f"Least Borrowed Book: '{least_borrowed_book}' with {book_borrowed_days[least_borrowed_book]} days.")
        
        total_days = sum(book_borrowed_days.values())  # Sum all borrowed days
        total_books = len(book_borrowed_days)  # Number of books
        
        average_days = total_days / total_books 
        
        print(f"\nAverage number of days books were borrowed: {average_days:.2f} days.")

        unique_titles = list(book_borrowed_days.keys())  # Extract the keys (unique titles) from the dictionary
        # returns a view of the dictionary's keys, which are the unique book titles. By converting this view to a list, we can easily print or use the unique titles.
        print("\nUnique titles of all borrowed books:")
        for title in unique_titles:
            print(f"'{title}'")

        sorted_books = sorted(book_borrowed_days.items(), key=lambda x: x[1], reverse=True)
        #  to sort the list of tuples based on the second element (borrowed days). im
        print("\nBooks sorted by borrowed days (descending):")
        for title, days in sorted_books:
            print(f"'{title}' - {days} days")
    else:
        print("\nNo books were entered.")

# Step 8: Call the function to start accepting input
accept_books()



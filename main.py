# Library Management System

# Books Name with their Authors and Book ID
books_library = {
    'the lord of the rings': {'Author': 'J.R.R. Tolkien', 'Book ID': 1011},
    'pride and prejudice': {'Author': 'Jane Austen', 'Book ID': 1012},
    'moby dick': {'Author': 'Herman Melville', 'Book ID': 1013},  # Note corrected capitalization
    'to kill a mockingbird': {'Author': 'Harper Lee', 'Book ID': 1014},
    'the catcher in the rye': {'Author': 'J.D. Salinger', 'Book ID': 1015}
}

while True:
    print("\nLibrary Management System")
    print("1. Display All Books with Name, Author, & Book ID")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Check Out a Book")
    
    num_task = int(input("\nEnter the number of Task you want to perform: "))
    
    if num_task == 1:
        for book_name, book_info in books_library.items():
            print(f"\nBook Name: {book_name.title()}")  # Correctly capitalizes each word in the book name
            for key, value in book_info.items():
                print(f"{key}: {value}")

    elif num_task == 2:
        search_book = input("Enter Book Name: ").lower()  # Case-insensitive search
        # Search for a match in the dictionary keys
        for book_name in books_library:
            if search_book == book_name.lower():  # Case-insensitive comparison
                print(f"\nBook Name: {book_name.title()} is available, and their info is below:")
                display_search_book = books_library[book_name]
                for key, value in display_search_book.items():
                    print(f"{key}: {value}")
                break
        else:
            print(f"\nBook '{search_book.title()}' is not available.")

    elif num_task == 3:
        author_name = input("Enter Book Author Name: ").lower()
        for books, books_aut in books_library.items():
            for book, aut in books_library.values():
                print(books_library[book][author_name])



    else:
        print("Invalid option, try again.")

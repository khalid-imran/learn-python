class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' has been borrowed.")
        else:
            print(f"Book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book '{self.__title}' has been returned.")
        else:
            print(f"Book '{self.__title}' was not borrowed.")

    def view_book_info(self):
        print(f"Book ID: {self.__book_id} Title: {self.__title} Author: {self.__author} Availability: {self.__availability}\n")
    
    @property
    def book_id(self):
        return self.__book_id


def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if Library.book_list:
                for book in Library.book_list:
                    book.view_book_info()
            else:
                print("No books available in the library.")

        elif choice == "2":
            book_id = input("Enter the Book ID to borrow: ")
            found = False
            for book in Library.book_list:
                if book.book_id == book_id:
                    book.borrow_book()
                    found = True
                    break
            if not found:
                print("Invalid Book ID.")        
           
        elif choice == "3":
            book_id = input("Enter the Book ID to return: ")
            found = False
            for book in Library.book_list:
                if book.book_id == book_id:
                    book.return_book()
                    found = True
                    break
            if not found:
                print("Invalid Book ID.")    
                 
        elif choice == "4":
            print("Exiting the Library.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

Book("101", "Python Programming", "John Doe")
Book("102", "Data Structures", "Jane Smith")
Book("103", "Machine Learning", "Alan Turing")

menu()

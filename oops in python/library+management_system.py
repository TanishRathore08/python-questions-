# Book class to store book details

class Book:
    def __init__(self, book_id , title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

# Library class to manage books

class Library:
    def __init__(self):
        self.books = []    # list to store book objects

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)          # create a new book object
        self.books.append(book)
        print(f"Book added to the library.")

# methpd to display all books

    def display_books(self):
        if not self.books:   # check if book list is empty
            print("No books in the library.")
            return
        print("\nlibrary Books:")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"            # check book status

            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")  

# method to issue a book
    def issue_book(self, book_id):
        for book in self.books:                                                 # loop through book list
            if book.book_id == book_id:                                              # check for matching book id
                if not book.is_issued:                                                # check if book is available
                    book.is_issued = True                                                # mark book as issued 
                    print(f"Book '{book.title}' has been issued.")
                else:
                    print(f"Book '{book.title}' is already issued.")
                    return
        print("Book not found in the library.")

        
# method to return a book

    def  return_book(self, book_id):
        for book in self.books:                                             # loop through all books 
            if book.book_id == book_id:                             #check if bool id is matched
               if book.is_issued:                                         #check if boook is issued
                    book.is_issued = False                                 # mark book as available 
                    print("Book returned successfully")
               else:
                    print("this book is not issued")
               return
        print("Book not found")
            

# main function

def main():
    library = Library()                     # object create

    while True:
        print("\n===Library Management System===")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("enter thr choice")

        if choice == "1":
            book_id=input("enter the book id")
            title= input("enter the book title")
            author=input("enter the book author")
            library.add_book(book_id,title,author)            #call add_book method
        
        elif choice  =="2":
            library.display_books()

        elif choice =="3":
            book_id= input("enter book is to issue")
            library.issue_book(book_id)

        elif choice =="4":
            book_id= input("enter book is to return")
            library.return_book(book_id)
        
        elif choice =="5":
            print(" Thankyou for using this Library management system")
            break
        
        else:
            print("Invalid choice. please try again")

# entry point of the program

if __name__ == "__main__":
    main()       #  Call main function
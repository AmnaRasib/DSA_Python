class LibrarySearch:
    def __init__(self):
        self.books=[]
    def add_bookInfo(self):
        n=int(input("Enter the Number of books you want to add: "))
        for i in range(n):
            print(f"\nEnter information of book_{i+1}:")
            x=input(f"Enter the book Title: ")
            y=input("Enter Author of book: ")
            self.books.append([x,y])
        print("\n")
        for j,book in enumerate  (self.books,1):
           print(f"Information of {j}_ book: Title: {book[0]}, Author: {book[1]}")
    def Search_book(self):
        s=input("\nEnter the Book title for search: ")
        found=False
        for book in self.books:
            if s.lower()==book[0].lower():
                print(f"Book found: Title: {book[0]}, Author: {book[1]}")
                found= True
                break
        if not found:
            print("Sorry! book is not found.")

l=LibrarySearch()
l.add_bookInfo()
l.Search_book()
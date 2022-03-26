class Library:
    def __init__(self,list,name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}
    def displayBooks(self):
        print(f"We have following Books in our library : {self.name}")
        for book in self.bookslist:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update(({book:user}))
            self.bookslist.remove(book)
            print("Lender - Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    def addBook(self,book):
        self.bookslist.append(book)
        print("Book has been added to the book list")
    def returnBook(self,book):
        if book not in self.bookslist:
            a = book
            self.bookslist.append(a)
            self.lendDict.pop(a)
            print("Successfully Returned")
        else:
            print("Book is not Successfully Returned")

if __name__ == '__main__':
    Bhuvi = Library(['Python','C++',"C#","English Communication"],"TMU")

    while(True):
        print(f"Welcome to the {Bhuvi.name} Library.")
        print("Please Enter Your Number of Choice - ")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book : ")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            Bhuvi.displayBooks()
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend : ")
            user = input("Enter Your Name : ")
            Bhuvi.lendBook(user,book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add : ")
            Bhuvi.addBook(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return : ")
            Bhuvi.returnBook(book)
        else:
            print("Not a valid option")
        print("Press Q to quit and C to continue : ")
        user_choice1 = ""
        while(user_choice1!="c" and user_choice1!="q"):
            user_choice1 = input()
            if user_choice1 == "q":
                exit()
            elif user_choice1 == "c":
                continue
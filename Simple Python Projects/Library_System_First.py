class Library:
    def __init__(self,book_list,library_name):
        self.book_list = book_list
        self.library_name = library_name
        self.lend_record = {}

    def display_book(self):
        print(self.book_list)

    def add_book(self):
        book = input("Enter Book Name : ")
        self.book_list.append(book)

    def lend_book(self):
        book = input("Enter Book Name : ").capitalize()
        if book not in self.book_list:
            print("Please Enter Valid Input")
        if book in self.book_list:
            name = input("Enter Your Name : ")
            self.book_list.remove(book)
            self.lend_record[book] = name
        else:
            if self.lend_record.get(book):
                print(f"Book does not exist in library this book taken by {self.lend_record[book]}")

    def return_book(self):
        book = input("Enter Book Name : ").capitalize()
        if book in self.lend_record:
            self.book_list.append(book)
            del self.lend_record[book]
        else:
            print("Please Enter Valid Input")

if __name__ == '__main__':
        book_list = ["C++","Java","JavaScript","Python"]
        Bhuvi_Library = Library(book_list,'Bhuvi_Library')

        while True:
            user = input("\n D for Display Book , A for Add Book , L for Lend Book , R for Return Book , Q for Exit : ")
            if user == "Q" or user == "q":
                break
            elif user == "display" or user == "Display" or user == "D" or user == "d" or user == "DISPLAY":
                Bhuvi_Library.display_book()
            elif user == "add" or user == "Add" or user == "a" or user == "ADD" or user == "A":
                Bhuvi_Library.add_book()
            elif user == "lend" or user == "Lend" or user == "L" or user == "l":
                Bhuvi_Library.lend_book()
            elif user == "return" or user == "Return" or user == "R" or user == "r":
                Bhuvi_Library.return_book()

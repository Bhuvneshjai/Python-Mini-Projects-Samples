class Library:
    def __init__(self,books,name):
        self.book_name = books
        self.library_name = name
        self.dict = {}

    def display_book(self):
        print(self.library_name)
        print("The Available Books are : ")
        for i in self.book_name:
            print(i,end = " , ")
        print()

    def add_book(self):
        a = input("\t \t Please enter the name of the books you want to add : ")
        print("Adding")
        self.book_name.append(a)
        print("Successfully Added !")

    def lend(self):
        a = input("Enter the name of book you want to lend : ")
        b = input("Enter the name of the person who are lending : ")
        if a in self.book_name:
            print("OK , You can take it !")
            self.dict[a] = b
            self.book_name.remove(a)
        elif a in self.dict:
            taker = self.dict[a]
            print(f"Sorry ! It is already taken by {taker}")
        else:
            print("Sorry ! We don't have such a book")

    def return_book(self):
        ret = input("Enter the Book Name : ")
        if ret in self.dict:
            self.dict.pop(ret)
            self.book_name.append(ret)
            print("Successfully Returned")
        else:
            print("You have not lent it")

library = Library(["Java Core","Python for Beginners","NodeJS","Introduction to WebDev","C++","Python","C"],"Bhvui_Library")

while True:
    inp = input("Enter D for Display Books \n Enter L for Lend Books \n Enter A for Add Books \n Enter R for Return Books \n Enter Q for Exit : ")
    if inp == "d" or inp == "D" or inp == "Display" or inp == "display":
        library.display_book()
    elif inp == "l" or inp == "L" or inp == "Lend" or inp == "lend":
        library.lend()
    elif inp == "a" or inp == "A" or inp == "Add" or inp == "ADD":
        library.add_book()
    elif inp == "r" or inp == "R" or inp == "Return" or inp == "return":
        library.return_book()
    elif inp == "Q" or inp == "q" or inp == "Quit" or inp == "QUIT":
        break
    else:
        print("Invalid Options ! ")
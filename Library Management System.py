from user_db import *
import random

class Library():
    def __init__(self,max_books, filename= "Books.txt", mode= "a+"):
        try:
            self.book_file = open(filename,mode)
        except FileNotFoundError:
            print("Error: File not found!")
        except IOError:
            print("Error: Unable to open file!")

        self.used_ids = set()
        self.id_dictionary = {}
        self.max_books = max_books
        self.count = 0

    def generate_unique_id(self):
        while True:
            book_id = (random.randint(1000, 9999))
            if book_id not in self.used_ids:
                self.used_ids.add(book_id)
                return book_id
    
    def list_books(self):
       self.book_file.seek(0)
       content = self.book_file.read()
       book_list = content.splitlines()
       self.used_ids = set()

       if not book_list:
           print("There is no book in the library.")

       for book in book_list:
            book_id = book.split(",")[0]
            book_title= book.split(",")[1]
            book_author = book.split(",")[2]
            if book_id not in self.used_ids:
                self.used_ids.add(book_id)
                print(f"Book:{book_title}, Author:{book_author}")
                
    def add_book(self):
        if self.count >= self.max_books:
            print("Sorry, the library is full. No more books can be added. ")
            return None
        else:
            self.count +=1
            book_title = " ".join((input("Book Title:")).split()).lower().title()

            while True:
                book_author = " ".join((input("Book Author:")).split()).lower().title()
                if book_author.isalpha():
                    break
                else:
                    print("Invalid Information! Try Again.")

            while True:
                book_genre = " ".join((input("Book Genre:")).split()).lower().title()
                if book_genre.isalpha():
                    break
                else:
                    print("Invalid Information! Try Again.")

            while True:
                try:
                    first_release_year = int((input("First Release Year:")).strip(" "))
                    break
                except ValueError:
                    print("Error: Invalid number input!")

            while True:
                try:
                    number_of_pages = int((input("Number Of Pages:")).strip(" "))
                    break
                except ValueError:
                    print("Error: Invalid number input!")

            book_info = [book_title,book_author,book_genre,first_release_year,number_of_pages]
            
            if tuple(book_info) not in self.id_dictionary:
                book_id = self.generate_unique_id()
                self.id_dictionary[tuple(book_info)] = book_id
            else:
                book_id = self.id_dictionary[tuple(book_info)]

            book_info.insert(0,book_id)
            info = ",".join(map(str, book_info))
            self.book_file.write(info + "\n" )
            self.book_file.flush()
            print("The book added succesfully!")

    def remove_book(self):
        book_title = input("Book Title:")
        book_title = " ".join(book_title.split()).lower().title()
        self.book_file.seek(0)
        content = self.book_file.read()
        book_list = content.splitlines()
        
        for book in book_list:
            book_title_list = []
            book_title_list.append(book.split(",")[1])
        
        if book_title not in book_title_list:
            print("The book not found in the library!")
            return None
        else:
            for book in book_list:
                if book.split(",")[1] == book_title:
                    book_id = book.split(",")[0]
                    i = book_list.index(book)
                    break

            for book in book_list:
                if book.split(",")[1] == book_title:
                    if book.split(",")[0] != book_id:
                        while True:
                            try: 
                                book_id = input("""There are multiple books with the same name and different id.
                                            Please enter the ID of the book you want to remove.""")
                                book_id = book_id.strip(" ")
                                book_id = int(book_id)
                                break
                            except ValueError:
                                print("Error: Invalid number input!")
                        break

            for book in book_list:
                if book.split(",")[0] == str(book_id):
                    i = book_list.index(book)
                    book_list.remove(book_list[i])
                    break

            self.book_file.truncate(0)
            for book in book_list:
                self.book_file.write(book + "\n")
            self.book_file.flush()
            print("The book removed succesfully!")
        
    def book_info(self):
        stock_dict = {"Book Info" : "Number Of Books"}
        self.book_file.seek(0)
        content = self.book_file.read()
        book_list = content.splitlines()

        for i in book_list:
            if i in stock_dict.keys():
                stock_dict[i] += 1
            else:
                stock_dict[i] = 1
        print(stock_dict)
    
    def print_menu(self):
        print("""
        1- Login
        2- Sign Up
        3- Quit
        """)

    def login_menu(self):
        print("""
        *** MENU*** 
        1) List Books 
        2) Add Book 
        3) Remove Book
        4) Book Info
        5) Quit
        """)

    def __del__(self):
        self.book_file.close()    

lib = Library(1000)
create_table()

while True:
    lib.print_menu()
    choice1 = input("Choice:")
    
    if choice1 == "1":
        username = input("Username:")
        search = search_username(username)
        if search == None:
            print("User not found!")
            continue
        password = input("Password:")
        if password == search[4]:
            while True:
                print("Welcome to the Library Management System!")
                lib.login_menu()
                choice2 = input("Choise:")
                if choice2   == '1':
                    lib.list_books()
                elif choice2 == '2':
                    lib.add_book()
                elif choice2 == '3':
                    lib.remove_book()
                elif choice2 == '4':
                    lib.book_info()
                elif choice2 == '5':
                    break
                else:
                    print("Wrong choise! Try again")
        else:
            print("Wrong password!")
    elif choice1 == "2":
        name = input("First Name:")
        lastname = input("Last Name:")
        username = input("Username:")
        password = input("Password:")
        search = search_username(username)
        if search != None:
            print("There is already an account with this username!")
            continue
        else:
            insert(name,lastname,username,password)
            print("Registration completed succesfully.")
    elif choice1 == "3":
        break
    else:
        print("Wrong choise! Try again")
import os
import time
from .helper import get_book_input

class Library:
    #Constructor for the Library class
    def __init__(self, file_name):
        #Stores the file name inside of the class
        self.file_name = file_name

        #Creates the file if it does not exists 
        self.books_file = open(file_name, "a+", encoding='utf-8')


    #Deconstructor for the Library class
    def __del__(self):
        print("-" * 77)

        #Closes the file
        self.books_file.close()
        print("Libraria is closing...")
        
    def read_file_content(self):
        #The list we are gonna store the books before putting them into a list
        books = []
        with open(self.file_name, "r", encoding='utf-8') as file:
            for line in file.readlines():
                book = []
                for part in line.split(","):
                    if(part[-1:] == "\n"):
                        book.append(part[:-1])
                    else:
                        book.append(part)
                books.append(book)
        return books
    
    def append_to_file(self, string):
        if(string != ""):
            self.books_file.write("\n" + string)
        self.books_file.flush()
        os.fsync(self.books_file.fileno())

    def list_books(self):

        books = self.read_file_content()
        print("-" * 77)
        print("  ID  |{} Book Name{}|{} Author{}|{} Year{}|{} Page".format(8 * " ",13 * " ",5 * " ",9 * " ",""," " * 4,""))
        id = 0;
        for line in books:
            string =  " " + str(id) + " " * (5 - len(str(id))) + "| "
            id+=1
            string += line[0] + ((30 - len(line[0])) * " " + "| ")
            string += line[1] + ((20 - len(line[1])) * " " + "| ")
            string += line[2] + ((8 - len(line[2])) * " " + "| ")
            string += line[3] + ((8 - len(line[3])) * " ")
            print(string)
        return ""


    def add_books(self):

        print("-" * 77)

        title,author,release_year,page_number = get_book_input()

        book_text = f"{title},{author},{release_year},{page_number}"

        self.append_to_file(book_text)

        return "Book has been successfully added to the list!"

    def remove_books(self):
        print("-" * 77)
        books = self.read_file_content()
        title = ""
        while(title == ""):
            title = input(" Enter the  ID/Title of  the   book: ")
        
        bookfound = False
        returnText,string,bookName = "","",""
        if(title.isnumeric() and int(title) >= len(books)):
            returnText = f"Specified book with index {title} does not exist!"
        elif(title.isnumeric() and int(title) < len(books)):
            for i, book in enumerate(books):
                if(i == int(title)):
                    bookfound = True
                    bookName = book[0]
                else:
                    string += f"{book[0]},{book[1]},{book[2]},{book[3]}"
                    string += "\n"
            string = string[:-1]
            returnText = f"The book '{bookName}' removed from the database!" if bookfound else f"Specified book with index {title} does not exist!"
        else:
            string = ""
            for book in books:
                if(book[0] == title):
                    bookfound = True
                else:
                    string += f"{book[0]},{book[1]},{book[2]},{book[3]}"
                    string += "\n"
            #Removes the last \n
            string = string[:-1]
            returnText = f"The book '{title}' removed from the database!" if bookfound else f"Specified book '{title}' does not exist!"
        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.write(string)
            file.flush()
        #return string
        return returnText

        return "FUCK"
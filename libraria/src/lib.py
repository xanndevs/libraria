import os
import time

class Library:
    #Constructor for the Library class
    def __init__(self, file_name):
        #Stores the file name inside of the class
        self.file_name = file_name

        #Creates the file if it does not exists 
        self.books_file = open(file_name, "a+", encoding='utf-8')


    #Deconstructor for the Library class
    def destruct(self):
        #Closes the file
        self.books_file.close()
        print("Libraria is closing...")
        time.sleep(3)
        exit()
        

    def list_books(self):

        #The list we are gonna store the book before printing it into a list
        self.books = []
        with open(self.file_name, "r", encoding='utf-8') as file:
            for line in file.readlines():
                book = []
                for part in line.split(","):
                    if(part[-1:] == "\n"):
                        book.append(part[:-1])
                    else:
                        book.append(part)
                self.books.append(book)
            print("-" * 77)
            print("  ID  |{} Book Name{}|{} Author{}|{} Year{}|{} Page".format(8 * " ",13 * " ",5 * " ",9 * " ",""," " * 4,""))
            id = 0;
            for line in self.books:
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
        title,author,release_year,page_number = "","","",""
        while(title == ""):
            title = input(" Enter the   title   of  the   book: ")
        while(author == ""):
            author = input(" Enter the   author  of  the   book: ")
        while(release_year == "" or not release_year.isnumeric()):
            release_year = input(" Enter the release year of the book: ")
        while(page_number == "" or not page_number.isnumeric()):
            page_number = input(" Enter the page number  of the book: ")

        book_text = f"{title},{author},{release_year},{page_number}"

        
        self.books_file.write("\n" + book_text)
        self.books_file.flush()
        os.fsync(self.books_file.fileno())

        return "Book has been successfully added to the list!"

    def remove_books(self):
        print("")
        return "FUCK"
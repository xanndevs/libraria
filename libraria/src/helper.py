import os

def clear_screen():
    #Clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("{}Welcome to Libraria{}".format(29 * " ",30 * " "))

def get_book_input():
    title,author,release_year,page_number = "","","",""
    while(title == "" or len(title) > 30):
        title = input(" Enter the   title   of  the   book: ")
    while(author == "" or len(title) > 20):
        author = input(" Enter the   author  of  the   book: ")
    while(release_year == "" or not release_year.isnumeric()):
        release_year = input(" Enter the release year of the book: ")
    while(page_number == "" or not page_number.isnumeric()):
        page_number = input(" Enter the page number  of the book: ")

    return title,author,release_year,page_number
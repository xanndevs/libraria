import os

def clear_screen():
    #Clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("{}Welcome to Libraria".format(29 * " "))

def get_book_input():
    title,author,release_year,page_number = "","","",""
    while(len(title) > 30 or len(title) <= 1):
        clear_screen()
        print("\n Add a Book to the List\n")
        blue_line()

        title = input(" Enter the   title   of  the   book: ")
    title = str("".join(title.split(",")))
    while(len(author) > 20 or len(author) <= 1):
        clear_screen()
        print("\n Add a Book to the List\n")
        blue_line()

        author = input(" Enter the   author  of  the   book: ")
    author = str("".join(author.split(",")))
    
    while(release_year == "" or not release_year.isnumeric()):
        clear_screen()
        print("\n Add a Book to the List\n")
        blue_line()

        release_year = input(" Enter the release year of the book: ")
    while(page_number == "" or not page_number.isnumeric()):
        clear_screen()
        print("\n Add a Book to the List\n")
        blue_line()
        page_number = input(" Enter the page number  of the book: ")

    return title,author,release_year,page_number

def blue_line():
    print("\033[1;94m" + "-" * 77 + "\033[0m")


from ..src.lib import Library

# Path to the books.txt file
file_name = "./libraria/books.txt"

# Create an instance of the BookParser class
parser = Library(file_name)

# Parse the books from the file
books = parser.list_books()

parser.add_books()



parser.exitLibrary("Library")
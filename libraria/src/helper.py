import os

def clear_screen():
    #Clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("{}Welcome to Libraria{}".format(29 * " ",30 * " "))


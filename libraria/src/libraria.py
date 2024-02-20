import keyboard
import os
import time
from .lib import Library
from .helper import clear_screen, blue_line


class Libraria:

    def __init__(self):

        #Creates the Library class
        file_name = "./libraria/books.txt"
        self.lib = Library(file_name)
        #self.flask_web = WebInterface()

        #The list of operations
        self.operations = {
            0:[self.lib.list_books, "List Books", "List of the Books"],
            1:[self.lib.add_books, "Add Books", "\n Add a Book to the List"],
            2:[self.lib.remove_books, "Remove Books", "\n Remove a Book from the List"],
            3:[self.wip, "Switch to Web", "\n This option is still in development"],
            4:[self.osexit, "Exit Libraria", "\n Exitting Libraria"]
        }
        self.option = 1

        #Cleans and makes the screen ready for the rest of the operations
        #clear_screen()

        #Draws the operations list 
        self.decrease_option()
        #self.operation_list()

        #Adds event listeners to the arrow keys
        self.add_keyboard_event()
        keyboard.wait('esc')
        self.osexit()

    def operation_list(self):
        blue_line()
        string = " "
        for i in range(len(self.operations)):
            string += "\n" if i % 3 == 0 else ""
            string += (("\033[1;94m->\033[0m" if i == self.option else "  ") + self.operations.get(i)[1]) + ((24 - len(self.operations.get(i)[1])) * " ")
        print(string)

    def redraw_options(self):
        clear_screen()
        print("\n " + self.operations.get(0)[2])
        self.operations.get(0)[0]()
        self.operation_list()

    def increase_option(self):
        if(self.option + 1 == len(self.operations)):
            return
        self.option += 1
        
        #Redraws the screen
        self.redraw_options()

    def decrease_option(self):
        if(self.option == 0):
            return
        self.option -= 1
        
        #Redraws the screen
        self.redraw_options()

    def handle_enter(self):
        clear_screen()

        keyboard.unhook_all_hotkeys()
        offscreenchoice = input("It looks like someone is trying to some other things...\n" + 
                                "Hit enter to continue {}.\nEnter 'q' to cancel the action: ".format(self.operations.get(self.option)[1]))
        
        if (offscreenchoice == 'q'):
            self.redraw_options()
            time.sleep(0.15)
            self.add_keyboard_event()
            return
        clear_screen()
        


        #exit()

        print(" " + self.operations.get(self.option)[2])
        self.operations.get(0)[0]()

        #Actual function running stage
        notification_string = ""
        if self.option != 0:
            notification_string = self.operations.get(self.option)[0]()
        
        self.redraw_options()
        print("\n" + notification_string)
        
        time.sleep(0.15)
        self.add_keyboard_event()

    def add_keyboard_event(self):
        self.rKey = keyboard.add_hotkey('right', self.increase_option)
        self.lKey = keyboard.add_hotkey('left', self.decrease_option)
        self.eKey = keyboard.add_hotkey('enter', self.handle_enter)
        self.escKey = keyboard.add_hotkey('esc', self.osexit)

    def wip(self):
        return "This option is still in early development"
    
    def osexit(self):
        
        blue_line()
        del self.lib
        del self
        print("\nGoodbye!\n")
        time.sleep(2)
        os._exit(0)
        return "Exitting failed!"    
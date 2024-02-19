from .lib import Library
import keyboard
import time
import sys
from .helper import clear_screen


class Libraria:

    def __init__(self):

        #Creates the Library class
        file_name = "./libraria/books.txt"
        self.lib = Library(file_name)
        #self.flask_web = WebInterface()

        #The list of operations
        self.operations = {
            0:[self.lib.list_books, "List Books", "List of the Books"],
            1:[self.lib.add_books, "Add Books", "Add a Book to the List"],
            2:[self.lib.remove_books, "Remove Books", "Remove a Book from the List"],
            3:[self.wip, "Switch to Web", "This option is still in development"],
            4:[self.__del__, "Exit Libraria", "Goodbye!"]
        }
        self.option = 1

        #Cleans and makes the screen ready for the rest of the operations
        #clear_screen()

        #Draws the operations list 
        self.decrease_option()
        #self.operation_list()

        #Adds event listeners to the arrow keys
        self.add_keyboard_event()
        keyboard.wait('q')

        

    def operation_list(self):
        print("-" * 77)
        string = " "
        for i in range(len(self.operations)):
            string += "\n" if i % 3 == 0 else ""
            string += (("->" if i == self.option else "  ") + self.operations.get(i)[1]) + ((24 - len(self.operations.get(i)[1])) * " ")
        print(string)

    def pass_option(self):
        clear_screen()
        print("\n " + self.operations.get(0)[2])
        self.operations.get(0)[0]()
        self.operation_list()

    def increase_option(self):
        if(self.option + 1 == len(self.operations)):
            return
        self.option += 1
        
        self.pass_option()

    def decrease_option(self):
        if(self.option == 0):
            return
        self.option -= 1
        
        self.pass_option()

    def handle_enter(self):
        clear_screen()

        keyboard.unhook_all_hotkeys()
        offscreenchoice = input("It looks like someone is trying to some other things...\n" + 
                                "Hit enter to continue {}.\nEnter 'q' to cancel the action: ".format(self.operations.get(self.option)[1]))
        
        if (offscreenchoice == 'q'):
            self.pass_option()
            time.sleep(0.15)
            self.add_keyboard_event()
            return
        clear_screen()
        
        notification_string = ""


        print(" " + self.operations.get(self.option)[2])
        self.operations.get(0)[0]()
        if self.option == 0:
            pass
        else:
            notification_string = self.operations.get(self.option)[0]()
        
        clear_screen()

        print("\n " + self.operations.get(0)[2])
        self.operations.get(0)[0]()
        self.operation_list()
        print("\n " + notification_string)
        time.sleep(0.15)
        self.add_keyboard_event()
        
    def add_keyboard_event(self):
        self.rKey = keyboard.add_hotkey('right', self.increase_option)
        self.lKey = keyboard.add_hotkey('left', self.decrease_option)
        self.eKey = keyboard.add_hotkey('enter', self.handle_enter)

    

    def __del__(self):
        keyboard.unhook_all_hotkeys()
        del self.lib
        sys.exit()

    def wip(self):
        return "This option is still in early development"
    
        
    
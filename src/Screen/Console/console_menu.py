from gui_helper import GetInput, CANCEL_LETTER

class ConsoleMenu:
    """ Represents a menu in the console window """
    
    def __init__(self, options):
        """ Build a menu from the options given """
        self.options = options
    
    def printMenu(self):
        """ Prints the menu """
        maxLength = len(str(len(self.options)))
        for option in self.options:
            optionNumber = str(self.options.index(option))
            optionNumber = optionNumber.zfill(maxLength)
            print "%s:%s" % (optionNumber, option)
    
    def runMenu(self):
        """ Runs the menu, printing and evaluating input until a valid option is chosen """
        valid = False
        while not valid:
            self.printMenu()
            input = raw_input().strip()
            valid = self.validateInput(input)
            
    def validateInput(self, input):
        """ Return if the input option is valid """
        return input in range(len(self.options)) or input == CANCEL_LETTER
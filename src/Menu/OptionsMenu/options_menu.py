from InputProcessor import bindings
from InputProcessor import commands

from Menu.text_menu_entry import TextMenuEntry

from kao_console.ascii import *

class OptionsMenu():
    """ Class to represent the options menu """
    keyStrings = {KAO_UP:"UP ARROW",
                  ord('W'):"W",
                  ord('w'):"w",
                  KAO_DOWN:"DOWN ARROW",
                  ord('S'):"S",
                  ord('s'):"s",
                  KAO_LEFT:"LEFT ARROW",
                  ord('A'):"A",
                  ord('a'):"a",
                  KAO_RIGHT:"RIGHT ARROW",
                  ord('D'):"D",
                  ord('d'):"d",
                  ESCAPE:"ESCAPE",
                  ENDL:"ENTER"}
                         
    cmdStrings = {commands.EXIT:"Exit",
                  commands.UP:"Up",
                  commands.DOWN:"Down",
                  commands.LEFT:"Left",
                  commands.RIGHT:"Right",
                  commands.SELECT:"Select",
                  commands.CANCEL:"Cancel"}
    
                         
    def __init__(self):
        """  """
        self.running = True
        self.heading = "Key Bindings"
        self.back = TextMenuEntry("Back", self.quit)
        self.back.select()
        
        self.keyBindings = self.getBoundKeyStrings()
                             
    def getBoundKeyStrings(self):
        """ Strings for Bound Keys """
        boundKeys = {commands.EXIT:[],
                     commands.UP:[],
                     commands.DOWN:[],
                     commands.LEFT:[],
                     commands.RIGHT:[],
                     commands.SELECT:[],
                     commands.CANCEL:[]}
        
        for key in bindings.keyBindings:
            boundKeys[bindings.keyBindings[key]].append(self.keyStrings[key])
            
        commandKeys = []
        for cmd in boundKeys:
            s = ""
            for binding in boundKeys[cmd]:
                s += binding
                if not binding == boundKeys[cmd][-1]:
                    s += ", "
            commandKeys.append(s)
            
        return commandKeys
        
    def quit(self, entry):
        """ Quits the Open Menu """
        self.running = False
        
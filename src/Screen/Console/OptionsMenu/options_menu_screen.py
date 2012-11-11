from InputProcessor import commands
from Screen.Console.screen import Screen

class OptionsMenuScreen(Screen):
    """ Options Menu screen """
    bindingsOrder = [commands.EXIT, commands.UP, commands.DOWN, commands.LEFT, commands.RIGHT, commands.SELECT, commands.CANCEL]
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        
    def draw(self, window):
        """ Draw the window """
        self.drawBindings(window)
        
    def drawBindings(self, window):
        """ Draw Bindings Text """
        self.drawCommands(window)
            
    def drawCommands(self, window):
        """ Draws the command """
        cmdsText = []
        cmdXRatio = 5.0/16
        yRato = 5.0
        max = 0
        for cmd in self.bindingsOrder:
            length = len(self.menu.cmdStrings[cmd])
            if length > max:
                max = length
                
        for cmd in self.bindingsOrder:
            diff = max - len(self.menu.cmdStrings[cmd])
            cmdText = "{0}{t.bold}{1}{t.normal}".format(" "*diff, self.menu.cmdStrings[cmd], t=window.terminal)
            cmdsText.append(cmdText)
            
        cmdCenter = self.getCenteredRect(window, (max, len(cmdsText)), 5.0/16, 14.0/32)
        window.draw(cmdsText, cmdCenter)
        
    def drawKeys(self, window, cmd, yRatio):
        """ Draws the binding """
        bindingXRatio = 8.0/16
        yRatio = 5.0
        
        self.font.set_bold(False)
        text = self.font.render(self.menu.keyBindings[cmd], 1, (10, 10, 10))
        textpos = text.get_rect(left = window.width*bindingXRatio, centery= window.height*(yRatio/32))
        window.draw(text, textpos)
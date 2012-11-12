from InputProcessor import commands
from Screen.Console.screen import Screen

class OptionsMenuScreen(Screen):
    """ Options Menu screen """
    bindingsOrder = [commands.EXIT, commands.UP, commands.DOWN, commands.LEFT, commands.RIGHT, commands.SELECT, commands.CANCEL]
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.title = ["____  __.             __________.__            .___.__                       ",
                        "|    |/ _|____ ___.__. \______   \__| ____    __| _/|__| ____    ____  ______",
                        "|      <_/ __ <   |  |  |    |  _/  |/    \  / __ | |  |/    \  / ___\/  ___/",
                        "|    |  \  ___/\___  |  |    |   \  |   |  \/ /_/ | |  |   |  \/ /_/  >___ \ ",
                        "|____|__ \___  > ____|  |______  /__|___|  /\____ | |__|___|  /\___  /____  >",
                        "        \/   \/\/              \/        \/      \/         \//_____/     \/ "]
        
    def draw(self, window):
        """ Draw the window """
        self.drawTitle(window)
        self.drawBindings(window)
        
    def drawTitle(self, window):
        """ Draws the title """
        titleLines = []
        for line in self.title:
            titleLines.append(window.terminal.yellow(line))
        window.draw(titleLines, (1, 0))
        
    def drawBindings(self, window):
        """ Draw Bindings Text """
        self.drawCommands(window)
        self.drawKeys(window)
            
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
            
        cmdCenter = self.getCenteredRect(window, (max, len(cmdsText)), cmdXRatio, 14.0/32)
        window.draw(cmdsText, cmdCenter)
        
    def drawKeys(self, window):
        """ Draws the binding """
        keysText = []
        bindingXRatio = 8.0/16
        yRato = 5.0
        max = 0
        for cmd in self.bindingsOrder:
            length = len(self.menu.keyBindings[cmd])
            if length > max:
                max = length
                
        for cmd in self.bindingsOrder:
            diff = max - len(self.menu.keyBindings[cmd])
            keyText = "{0}{1}".format(self.menu.keyBindings[cmd], " "*diff, t=window.terminal)
            keysText.append(keyText)
            
        keyCenter = self.getCenteredRect(window, (max, len(keysText)), bindingXRatio, 14.0/32)
        window.draw(keysText, keyCenter)
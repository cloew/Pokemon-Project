from InputProcessor import commands

from kao_gui.console.console_screen import ConsoleScreen

class OptionsMenuScreen(ConsoleScreen):
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
        
    def draw(self):
        """ Draw the window """
        self.drawTitle()
        self.drawBindings()
        
    def drawTitle(self):
        """ Draws the title """
        titleLines = []
        for line in self.title:
            titleLines.append(self.terminal.yellow(line))
        self.drawAtPosition(titleLines, (1, 0))
        
    def drawBindings(self):
        """ Draw Bindings Text """
        self.drawCommands()
        self.drawKeys()
            
    def drawCommands(self):
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
            cmdText = "{0}{t.bold}{1}{t.normal}".format(" "*diff, self.menu.cmdStrings[cmd], t=self.terminal)
            cmdsText.append(cmdText)
            
        self.drawCenteredText(cmdsText, (max, len(cmdsText)), cmdXRatio, 14.0/32)
        
    def drawKeys(self):
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
            keyText = "{0}{1}".format(self.menu.keyBindings[cmd], " "*diff, t=self.terminal)
            keysText.append(keyText)
            
        self.drawCenteredText(keysText, (max, len(keysText)), bindingXRatio, 14.0/32)
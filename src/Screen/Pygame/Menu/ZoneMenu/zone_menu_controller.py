from InputProcessor import commands
from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry
from Screen.Pygame.Menu.ZoneMenu.zone_menu_screen import ZoneMenuScreen

from kao_gui.pygame.pygame_controller import PygameController

class ZoneMenuController(PygameController):
    """ Controller for the Zone Menu """
    
    def __init__(self, lastController):
        """ Initialize the Zone Menu Controller """
        entries = [TextMenuEntry("Exit", self.exitZone)]
        self.menu = Menu(entries)
        self.lastController = lastController
        
        screen = ZoneMenuScreen(self.menu, lastController.screen)
        PygameController.__init__(self, screen, commands = {commands.UP:self.menu.up,
                                                            commands.DOWN:self.menu.down,
                                                            commands.EXIT:self.stopRunning,
                                                            commands.SELECT:self.menu.enter})
                                                            
    def exitZone(self, entry=None):
        """ Exit the Zone """
        self.lastController.stopRunning()
        self.stopRunning()
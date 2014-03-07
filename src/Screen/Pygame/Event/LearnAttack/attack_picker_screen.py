from kao_gui.pygame.pygame_screen import PygameScreen

class AttackPickerScreen(PygameScreen):
    """ Represents the screen for a Picking an Attack """
    
    def __init__(self, attacksMenu, lastScreen):
        """ Initialize the screen """
        PygameScreen.__init__(self)
        self.attacksMenu = attacksMenu
        self.lastScreen = lastScreen
        
    def drawSurface(self):
        """ Draws the screen """
        previousScreenSurface = self.lastScreen.draw()
        self.drawOnSurface(previousScreenSurface, left=0, top=0)
        
        menuSurface = self.attacksMenu.draw()
        self.drawOnSurface(menuSurface, left=.05, top=.7)
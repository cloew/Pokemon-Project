import sys

from resources.resource_manager import GetImagePath

def GetStartController():
    """ Return the controller to start the game """
    # try:
    from Screen.Pygame.Menu.MainMenu.main_menu_controller import MainMenuController
    # except ImportError as error:
        # print error
        # from Menu.MainMenu.main_menu_controller import MainMenuController
    return MainMenuController()
    
def GetWindow():
    """ Return the proper window for the game """
    # try:
    from kao_gui.pygame.window import BuildWindow
    from InputProcessor import pygame_bindings
    window = BuildWindow(width=640, height=480, caption='Pokemon', 
                            iconFilename=GetImagePath('pokeball3.bmp'),
                            bindings=pygame_bindings.keyBindings)
    # except ImportError as error:
        # print error
        # from Screen.Console.window import window
    return window
    
def main(argv):
    """ Start the game """
    window = GetWindow()
    startController = GetStartController()
    try:
        startController.run()
    finally:
        window.close()

if __name__ == "__main__":
    main(sys.argv[1:])
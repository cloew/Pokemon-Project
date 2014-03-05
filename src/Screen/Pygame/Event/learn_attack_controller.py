from Battle.battle_message import BattleMessage

from Screen.Pygame.Event.learn_attack_screen import LearnAttackScreen
from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController

from kao_gui.pygame.pygame_controller import PygameController

class LearnAttackController(PygameController):
    """ Controller for Learning an Attack """
    
    def __init__(self, event, lastScreen):
        """ Initialize the Learn Attack Controller """
        screen = LearnAttackScreen(lastScreen)
        PygameController.__init__(self, screen)
        self.event = event
        self.done = False
        
    def performGameCycle(self):
        """ Perform the learn attack loop """
        while not self.done:
            messages = self.event.getTryToLearnMessages()
            for message in messages:
                self.runController(MessageBoxController(BattleMessage(message), self.screen))
            self.done = True
        self.stopRunning()
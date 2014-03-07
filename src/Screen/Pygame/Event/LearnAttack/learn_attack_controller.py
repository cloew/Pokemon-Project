from Battle.battle_message import BattleMessage

from Screen.Pygame.Event.LearnAttack.learn_attack_screen import LearnAttackScreen
from Screen.Pygame.Event.LearnAttack.attack_picker_controller import AttackPickerController
from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController
from Screen.Pygame.YesNo.yes_no_controller import YesNoController

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
        while not self.done and self.isRunning():
            messages = self.event.getTryToLearnMessages()
            self.presentMessages(messages[:-1])
                
            if self.userWantsToForget(messages[-1]):
                attack = self.pickAttackToForget()
                if attack is not None:
                    self.done = True
                    messages = self.event.learnAndReplace(attack)
                    self.presentMessages(messages)
            elif self.userWantsToStopLearning(self.event.getStopLearningMessage()):
                    self.done = True
                        
        self.stopRunning()
        
    def userWantsToForget(self, message):
        """ Return if the Player wants to forget a move """
        return self.getYesNoResponse(message)
        
    def userWantsToStopLearning(self, message):
        """ Return if the user wants to stop learning the new attack """
        return self.getYesNoResponse(message)
        
    def pickAttackToForget(self):
        """ Return the Attack the user would like to replace """
        pickAttackController = AttackPickerController(self.event.pokemon, self.screen)
        self.runController(pickAttackController)
        return pickAttackController.attack
        
    def getYesNoResponse(self, message):
        """ Return the Yes/No Response """
        yesNoController = YesNoController(BattleMessage(message), self.screen)
        self.runController(yesNoController)
        return yesNoController.answer
        
    def presentMessages(self, messages):
        """ Present the given messages """
        for message in messages:
            self.runController(MessageBoxController(BattleMessage(message), self.screen))
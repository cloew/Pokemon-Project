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
            for message in messages[:-1]:
                self.runController(MessageBoxController(BattleMessage(message), self.screen))
                
            yesNoController = YesNoController(BattleMessage(messages[-1]), self.screen)
            self.runController(yesNoController)
            if yesNoController.answer:
                pickAttackController = AttackPickerController(self.event.pokemon, self.screen)
                self.runController(pickAttackController)
                if pickAttackController.attack is not None:
                    self.done = True
                    messages = self.event.learnAndReplace(pickAttackController.attack)
                    for message in messages:
                        self.runController(MessageBoxController(BattleMessage(message), self.screen))
            else:
                message = BattleMessage(self.event.getStopLearningMessage())
                yesNoController = YesNoController(message, self.screen)
                self.runController(yesNoController)
                if yesNoController.answer:
                    self.done = True
                        
        self.stopRunning()
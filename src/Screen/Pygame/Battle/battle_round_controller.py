from InputProcessor import commands
from Screen.Pygame.Battle.battle_message_box import BattleMessageBox
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.ActionMenu.action_menu_controller import ActionMenuController

class BattleRoundController(Controller):
    """ Controller for Battle Rounds """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Round Controller """
        Controller.__init__(self)
        self.battle = battle
        self.screen = screen
        self.cmds = {commands.SELECT:self.battle.removeMessageFromQueue}
        
    def update(self):
        """ Tells the battle object what to perform """
        if self.battle.noMessages():
            pokemonActions = {}
            for pokemon in self.battle.playerSide.pkmnInPlay:
                actionMenuController = ActionMenuController(pokemon, self.battle, self.screen)
                actionMenuController.run()
                pokemonActions[pokemon] = actionMenuController.action
            
            self.screen.setBottomView(BattleMessageBox(self.battle))
            self.battle.performRound(pokemonActions)
            if self.battle.over:
                self.stopRunning()
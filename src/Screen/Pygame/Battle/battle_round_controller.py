from InputProcessor import commands
from Screen.Pygame.Battle.battle_message_box import BattleMessageBox
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.ActionMenu.action_menu_controller import ActionMenuController
from Screen.Pygame.Menu.ActionMenu.SwitchMenu.switch_menu_controller import SwitchMenuController

class BattleRoundController(Controller):
    """ Controller for Battle Rounds """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Round Controller """
        Controller.__init__(self)
        self.battle = battle
        self.screen = screen
        self.cmds = {commands.SELECT:self.battle.removeMessageFromQueue}
        
        self.coroutine = self.performEntireRound()
        self.coroutine.next()
        
    def update(self):
        """ Tells the battle object what to perform """
        if self.battle.noMessages():
            self.coroutine.send(None)
                    
            if self.battle.over:
                self.stopRunning()
                
    def performEntireRound(self):
        """ Perform an Entire Round """
        while not self.battle.over:
            self.performRound()
            yield
            self.refillSides()
            yield
                
    def performRound(self):
        """ Perform a Single Round """
        pokemonActions = {}
        for pokemon in self.battle.playerSide.pkmnInPlay:
            if not pokemon.actionLock:
                actionMenuController = ActionMenuController(pokemon, self.battle, self.screen)
                actionMenuController.run()
                pokemonActions[pokemon] = actionMenuController.action
        
        self.screen.setBottomView(BattleMessageBox(self.battle))
        self.battle.performRound(pokemonActions)
        
    def refillSides(self):
        """ Refill the Battle Sides """
        pokemonReplacements = {}
        if self.battle.playerSide.hasMorePokemon():
            for pokemon in self.battle.playerSide.pkmnInPlay:
                if pokemon.fainted():
                    switchMenuController = SwitchMenuController(pokemon)
                    switchMenuController.run()
                    pokemonReplacements[pokemon] = switchMenuController.action.pkmnToSwitchTo
                    
        self.battle.refillSides(pokemonReplacements)
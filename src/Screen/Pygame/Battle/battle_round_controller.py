from InputProcessor import commands
from Screen.Pygame.Battle.battle_message_box import BattleMessageBox
from Screen.Pygame.Menu.ActionMenu.action_menu_controller import ActionMenuController
from Screen.Pygame.Menu.ActionMenu.SwitchMenu.switch_menu_controller import SwitchMenuController

from kao_gui.pygame.pygame_controller import PygameController

class BattleRoundController(PygameController):
    """ Controller for Battle Rounds """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Round Controller """
        self.battle = battle
        cmds = {commands.SELECT:self.battle.removeEventFromQueue}
        PygameController.__init__(self, screen, commands=cmds)
        
        self.coroutine = self.performEntireRound()
        
    def performGameCycle(self):
        """ Tells the battle object what to perform """
        if self.battle.noEvents():
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
                self.runController(actionMenuController)
                if actionMenuController.action is None:
                    return
                else:
                    pokemonActions[pokemon] = actionMenuController.action
        
        self.screen.setBottomView(BattleMessageBox(self.battle, self.getWindow().width*.9, self.getWindow().height*.3))
        self.battle.performRound(pokemonActions)
        
    def refillSides(self):
        """ Refill the Battle Sides """
        pokemonReplacements = {}
        if self.battle.playerSide.hasMorePokemon():
            for pokemon in self.battle.playerSide.pkmnInPlay:
                if pokemon.fainted():
                    switchMenuController = SwitchMenuController(pokemon, cancellable=False)
                    self.runController(switchMenuController)
                    pokemonReplacements[pokemon] = switchMenuController.action.pkmnToSwitchTo
                    
        self.battle.refillSides(pokemonReplacements)
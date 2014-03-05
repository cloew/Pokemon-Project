from InputProcessor import commands

from Screen.Pygame.Event.event_handler import PerformEvents
from Screen.Pygame.Menu.ActionMenu.action_menu_controller import ActionMenuController
from Screen.Pygame.Menu.ActionMenu.SwitchMenu.switch_menu_controller import SwitchMenuController

from kao_gui.pygame.pygame_controller import PygameController

class BattleRoundController(PygameController):
    """ Controller for Battle Rounds """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Round Controller """
        self.battle = battle
        PygameController.__init__(self, screen)
        
        self.coroutine = self.performEntireRound()
        
    def performGameCycle(self):
        """ Tells the battle object what to perform """
        self.screen.setBottomView(None)
        PerformEvents(self.battle.eventQueue, self)
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
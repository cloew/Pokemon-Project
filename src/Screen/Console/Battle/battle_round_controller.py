from Battle.battle_message import BattleMessage
from Screen.Console.Menu.ActionMenu.action_controller import ActionController
from Screen.Console.Menu.ActionMenu.SwitchMenu.switch_controller import SwitchController
from Screen.Console.MessageBox.message_box import MessageBox

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

class BattleRoundController(ConsoleController):
    """ Controller for a Battle Round """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Round Controller """
        self.battle = battle
        self.messageBox = MessageBox(BattleMessage(""))
        screen.messageBox = self.messageBox
        cmds = {ENDL:self.battle.removeMessageFromQueue}
        ConsoleController.__init__(self, screen, commands=cmds)
        
        self.coroutine = self.performEntireRound()
        
    def performGameCycle(self):
        """ Tells the battle object what to perform """
        if self.hasMessages() and self.newMessage():
            self.screen.messageBox = MessageBox(self.battle.messageQueue[0])
            
        elif self.battle.noMessages():
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
                actionMenuController = ActionController(pokemon, self.battle)
                self.runController(actionMenuController)
                if actionMenuController.action is None:
                    return
                else:
                    pokemonActions[pokemon] = actionMenuController.action
        
        self.screen.messageBox = self.messageBox
        self.battle.performRound(pokemonActions)
        
    def refillSides(self):
        """ Refill the Battle Sides """
        pokemonReplacements = {}
        if self.battle.playerSide.hasMorePokemon():
            for pokemon in self.battle.playerSide.pkmnInPlay:
                if pokemon.fainted():
                    switchMenuController = SwitchController(pokemon, cancellable=False)
                    self.runController(switchMenuController)
                    pokemonReplacements[pokemon] = switchMenuController.action.pkmnToSwitchTo
                    
        self.battle.refillSides(pokemonReplacements)
        
    def hasMessages(self):
        """ Returns if there are messages in the battle's queue """
        return len(self.battle.messageQueue) > 0

    def newMessage(self):
        """ Returns if the message on the top of the queue 
        is different than the current message """
        return not self.battle.messageQueue[0] == self.screen.messageBox.message
from gui_helper import PrintOppPokemon, PrintPlayerPokemon, GetInput, CANCEL_LETTER
from Screen.Console.switch_view import ConsoleSwitchScreen

from resources.constants import Constants

class ConsoleBattleScreen:
    """ Represents the Screen as a Console for a Battle """
    actions = [Constants.fightAction, Constants.switchAction, 
                   Constants.itemsAction, Constants.runAction]
    oneThruFour = ["1", "2", "3", "4"]
    cancelLetter = "/"
    
    def __init__(self, battle):
        """ Starts a Console Battle Screen """
        self.battle = battle
        
        self.doAction = {Constants.fightAction: self.fight, Constants.switchAction:self.switch, 
                                Constants.itemsAction:self.item, Constants.runAction: self.run}
        
    def introduce(self):
        """ Performs the introduction to the battle """
        oppTrainer = self.battle.getOppTrainer()
        
        print "%s challenges you to a Pokemon Battle!\n" % oppTrainer.getFullName()
        
    def printScreen(self):
        """ Prints the screen """
        oppPkmn = self.battle.getOppPkmn()
        playerPkmn = self.battle.getPlayerPkmn()
        print "\n"
        
        for pkmn in oppPkmn:
            PrintOppPokemon(pkmn.pkmn)
                 
        for pkmn in playerPkmn:
            PrintPlayerPokemon(pkmn.pkmn)
            
    def pickAction(self):
        """ Loops until user has decided on their action """
        donePicking = False
        while not donePicking:
            donePicking, ret = self.getAction()
            
        return ret
        
    def getAction(self):
        """ Lets the user pick their action for a turn in the Battle """
        print "What will you do?"
        print "1. FIGHT", "\t", "2. SWITCH"
        print "3. ITEMS", "\t", "4. RUN"
        
        i = int(GetInput(ConsoleBattleScreen.oneThruFour))
        
        return self.doAction[ConsoleBattleScreen.actions[i-1]]()
        
    def fight(self):
        """ Handles logic for fighting and stuff """
        self.printScreen()
        attacks = self.battle.getPlayerPkmn()[0].getAttacks()
        
        for i in range(len(attacks)):
            print "%i." % (i+1), attacks[i].name
            
        i = int(GetInput(ConsoleBattleScreen.oneThruFour))
        
        if i == CANCEL_LETTER:
            return False, None
        return True, [Constants.fightAction, attacks[i-1], self.battle.getPlayerPkmn()[0], self.battle.getOppPkmn()[0]]
        
    def switch(self):
        """ Switches Pokemon """
        screen = ConsoleSwitchScreen(self.battle.getPlayerTrainer(), self.battle.getPlayerPkmn())
        #valid, comps = screen.switch()
        return screen.switch()
        
    def item(self):
        """ Pick an item """
        print "Not implemented"
        return False, None
        
    def run(self):
        """ Run away, if possible """
        print "Not implemented"
        return False, None
        
    def reportAction(self, messages):
        """ Report the results of an action """
        if len(messages) is 0:
            return
            
        self.printScreen()
        self.reportMessages(messages)
        raw_input("Press 'Enter' to continue")
        
    def reportMessages(self, messages):
        """ Reports a sequence of messages """
        for message in messages:
            self.reportMessage(message)
        
    def reportMessage(self, message):
        """ Report a Single message """
        print message
    
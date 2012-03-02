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
            print pkmn.getCurrHP(), "/", pkmn.getStat("HP"), \
                    "\t", pkmn.getStatus().abbr, "\t", pkmn.getName()
                 
        for pkmn in playerPkmn:
            print pkmn.getName(), "\t", pkmn.getStatus().abbr, "\t", \
                    pkmn.getCurrHP(),  "/", pkmn.getStat("HP")
        
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
        
        i = int(ConsoleBattleScreen.getInput(ConsoleBattleScreen.oneThruFour))
        
        return self.doAction[ConsoleBattleScreen.actions[i-1]]()
        
    def fight(self):
        """ Handles logic for fighting and stuff """
        self.printScreen()
        attacks = self.battle.getPlayerPkmn()[0].getAttacks()
        
        for i in range(len(attacks)):
            print "%i." % (i+1), attacks[i].name
            
        i = int(ConsoleBattleScreen.getInput(ConsoleBattleScreen.oneThruFour))
        
        if i == ConsoleBattleScreen.cancelLetter:
            return False, None
        return True, [Constants.fightAction, attacks[i-1], self.battle.getPlayerPkmn()[0], self.battle.getOppPkmn()[0]]
        
    def switch(self):
        """ Switches Pokemon """
        print "Not implemented"
        return False, None
        
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
        
        for message in messages:
            self.reportMessage(message)
        
        raw_input("Press 'Enter' to continue")
        
    def reportMessage(self, message):
        """ Report a Single message """
        print message
    
    @staticmethod
    def getInput(validInput):
        """ Gets valid input from the user """
        valid = False
        while not valid:
            i = raw_input().strip()
            valid = ConsoleBattleScreen.validateInput(i, validInput)
        return i
        
    @staticmethod
    def validateInput(input, validInput):
        """ Validates that input entered is valid """
        return input in validInput or input == ConsoleBattleScreen.cancelLetter
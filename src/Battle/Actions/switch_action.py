from Battle.Actions.battle_action import BattleAction

class SwitchAction(BattleAction):
    """ Represents a battle action where the pokemon is switching """
    
    def __init__(self, user, pkmnToSwitchTo):
        """ Build an attack action """
        self.user = user
        self.switchPkmn = pkmnToSwitchTo
    
    def getPriority(self):
        """ Returns the Speed Priority of the Action """
        return 6
        
    def doAction(self):
        """ Performs the action """
        return self.user.sendOutPkmn(self.switchPkmn)
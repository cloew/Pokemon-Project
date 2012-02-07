from Battle.Actions.battle_action import BattleAction

class AttackAction(BattleAction):
    """ Represents a battle action where the pokemon is using an attack """
    
    def __init__(self, attack, user, target):
        """ Build an attack action """
        self.attack = attack
        self.user = user
        self.target = target
    
    def getPriority(self):
        """ Returns the Speed Priority of the Action """
        return self.attack.speedDelegate.priority
        
    def doAction(self):
        """ Performs the action """
        return self.attack.use(user, target)
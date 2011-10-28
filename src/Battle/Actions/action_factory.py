from Battle.Actions.attack_action import AttackAction
from resources.constants import Constants


class ActionFactory:
    """ Builds BattleActions """
    
    @staticmethod
    def buildActionFromType(actionParams):
        """ Builds an action based on the type as a string """
        actionType = actionParams[0]
        if actionType == Constants.fightAction:
            return AttackAction(actionParams[1])
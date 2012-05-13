from Battle.battle_view_controller import BattleViewController

class Marathon:
    """  Represents a trainer marathon """
    
    def __init__(self, name, trainers, description):
        """  """
        self.name = name
        self.trainers = trainers
        self.description = description
        
    def run(self, player):
        """ Runs the marathon """
        for cpu in self.trainers:
            BattleViewController().begin(player, cpu)
from Trainer.trainer_factory import TrainerFactory
from Zone.zone_factory import ZoneFactory

class Marathon:
    """  Represents a trainer marathon """
    
    def __init__(self):#, name, trainers, description, zone):
        """ Initialize the Marathon """
        self.name = "Kanto Gym Leaders"#name
        # self.trainers = [TrainerFactory.loadFromXML("Gym Leader", "Brock")]#trainers
        self.trainers = [TrainerFactory.loadFromXML("Leader", "Alex")]#trainers
        self.description = "Battle the Kanto Gym Leaders"#description
        self.zone = "Kanto Gym Leaders Marathon"#zone
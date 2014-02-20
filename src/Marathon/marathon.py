from Trainer.trainer_factory import TrainerFactory
from Zone.zone_factory import ZoneFactory

class Marathon:
    """  Represents a trainer marathon """
    
    def __init__(self):#, name, trainers, description, zone):
        """ Initialize the Marathon """
        self.name = "Kanto Gym Leaders"#name
        self.trainers = []
        self.description = "Battle the Kanto Gym Leaders"#description
        self.zoneName = "Kanto Gym Leaders Marathon"#zone
        self.zone = None
        
    def loadZone(self):
        """ Load the marathon zone """
        self.zone = ZoneFactory.getZone(self.zoneName)
        for person in self.zone.people:
            if hasattr(person, "trainer"):
                self.trainers.append(person.trainer)
        
        return self.zone
        
    def beaten(self):
        """ Return if the marathon has been beaten """
        return self.zone is not None and len([trainer for trainer in self.trainers if trainer.hasPokemon()]) == 0
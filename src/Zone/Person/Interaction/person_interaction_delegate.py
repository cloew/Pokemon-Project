from Zone.direction import GetOppositeDirection
from Zone.Interaction.interaction_delegate import InteractionDelegate

class PersonInteractionDelegate(InteractionDelegate):
    """ Interaction Delegate for a Zone Person """
    
    def __init__(self, message, callback=None):
        """ Initialize the Interaction delegate """
        self.message = message
        self.callback = callback
        
    def setTrainer(self, trainer):
        """ Sets the Trainer """
        self.trainer = trainer
        
    def interact(self, direction):
        """ Interact with the trainer """
        self.content.movementDelegate.direction = GetOppositeDirection(direction)
        InteractionDelegate.interact(self, direction)
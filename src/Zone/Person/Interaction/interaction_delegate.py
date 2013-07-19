from Zone.direction import GetOppositeDirection

class InteractionDelegate:
    """ Interaction Delegate for a Zone Person """
    
    def __init__(self, message, callback):
        """ Initialize the Interaction delegate """
        self.message = message
        self.callback = callback
        
    def setTrainer(self, trainer):
        """ Sets the Trainer """
        self.trainer = trainer
        
    def interact(self, direction):
        """ Interact with the trainer """
        self.trainer.direction = GetOppositeDirection(direction)
        if self.callback is not None:
            self.callback(self.trainer, self.message)
from Zone.direction import UP, DOWN, LEFT, RIGHT, GetTextFromDirection, GetOppositeDirection
from Zone.Person.Movement.movement_delegate import MovementDelegate

class Person:   
    """ Represents a person in a game zone """
    
    def __init__(self, tile, imageBaseName, interactionDelegate):
        """ Initialize the Person """
        self.tile = None
        self.setTile(tile)
        
        self.imageBaseName = imageBaseName
        
        self.interactionDelegate = interactionDelegate
        self.interactionDelegate.setTrainer(self)
        
        self.movementDelegate = MovementDelegate(self)
        
    def getImageBaseName(self):
        """ Return the base image name for the Trainer Position Wrapper """
        return "{0}_{1}".format(self.imageBaseName, GetTextFromDirection(self.movementDelegate.direction))
        
    def setTile(self, tile):
        """ Set the Trainer's current tile """
        if self.tile is not None:
            self.tile.setContents(None)
        self.tile = tile
        tile.setContents(self)
        
    def up(self):
        """ Move the Trainer up """
        self.movementDelegate.prepareToMove(UP)
        
    def down(self):
        """ Move the Trainer down """
        self.movementDelegate.prepareToMove(DOWN)
        
    def left(self):
        """ Move the Trainer left """
        self.movementDelegate.prepareToMove(LEFT)
        
    def right(self):
        """ Move the Trainer right """
        self.movementDelegate.prepareToMove(RIGHT)
        
    def stopMovingUp(self):
        """ Stop the Trainer from moving """
        self.movementDelegate.stopMoving(UP)
        
    def stopMovingDown(self):
        """ Stop the Trainer from moving """
        self.movementDelegate.stopMoving(DOWN)
        
    def stopMovingLeft(self):
        """ Stop the Trainer from moving """
        self.movementDelegate.stopMoving(LEFT)
        
    def stopMovingRight(self):
        """ Stop the Trainer from moving """
        self.movementDelegate.stopMoving(RIGHT)
        
    def interactWithAdjacentTile(self):
        """ Interact with an adjacent city """
        destination = self.getAdjacentTile(self.direction)
        if destination.contents is not None:
            destination.contents.interact(self.direction)
            
    def interact(self, direction):
        """ Interact with the trainer """
        self.interactionDelegate.interact(direction)
                
    def performGameTick(self):
        """ Perform a single game tick """
        self.movementDelegate.performGameTick()
            
    def isBattleable(self):
        """ Return if the person is Battleable """
        return False 
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
        self.up = self.makeMoveFunction(UP)
        self.down = self.makeMoveFunction(DOWN)
        self.left = self.makeMoveFunction(LEFT)
        self.right = self.makeMoveFunction(RIGHT)
        
        self.stopMovingUp = self.makeStopMovingFunction(UP)
        self.stopMovingDown = self.makeStopMovingFunction(DOWN)
        self.stopMovingLeft = self.makeStopMovingFunction(LEFT)
        self.stopMovingRight = self.makeStopMovingFunction(RIGHT)
        
    def getImageBaseName(self):
        """ Return the base image name for the Trainer Position Wrapper """
        return "{0}_{1}".format(self.imageBaseName, GetTextFromDirection(self.movementDelegate.direction))
        
    def setTile(self, tile):
        """ Set the Trainer's current tile """
        if self.tile is not None:
            self.tile.setContents(None)
        self.tile = tile
        tile.setContents(self)
        
    def makeMoveFunction(self, direction):
        def moveFunction():
            """ Move in the specified direction """
            self.movementDelegate.prepareToMove(direction)
        return moveFunction
        
    def makeStopMovingFunction(self, direction):
        def stopMovingFunction():
            """ Stop moving in the specified direction """
            self.movementDelegate.stopMoving(direction)
        return stopMovingFunction
        
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
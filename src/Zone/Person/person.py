from Zone.direction import UP, DOWN, LEFT, RIGHT, GetTextFromDirection, GetOppositeDirection
from Zone.Person.Movement.movement_delegate import MovementDelegate
from Zone.Person.Movement.movement_helper import MakeMoveFunction, MakeStopMovingFunction

class Person:   
    """ Represents a person in a game zone """
    
    def __init__(self, tile, imageBaseName, interactionDelegate):
        """ Initialize the Person """
        self.tile = tile
        self.setTile(tile)
        
        self.imageBaseName = imageBaseName
        
        self.interactionDelegate = interactionDelegate
        self.interactionDelegate.setTrainer(self)
        
        self.movementDelegate = MovementDelegate(self)
        self.up = MakeMoveFunction(self, UP)
        self.down = MakeMoveFunction(self, DOWN)
        self.left = MakeMoveFunction(self, LEFT)
        self.right = MakeMoveFunction(self, RIGHT)
        
        self.stopMovingUp = MakeStopMovingFunction(self, UP)
        self.stopMovingDown = MakeStopMovingFunction(self, DOWN)
        self.stopMovingLeft = MakeStopMovingFunction(self, LEFT)
        self.stopMovingRight = MakeStopMovingFunction(self, RIGHT)
        
    def getImageBaseName(self):
        """ Return the base image name for the Trainer Position Wrapper """
        return "{0}_{1}".format(self.imageBaseName, GetTextFromDirection(self.movementDelegate.direction))
        
    def setTile(self, tile):
        """ Set the Trainer's current tile """
        if self.tile is not None:
            self.tile.setContents(None)
        self.tile = tile
        if self.tile is not None:
            tile.setContents(self)
            
    def setInteractionCallback(self, callback):
        """ Set the Person's Interaction Callback """
        self.interactionDelegate.callback = callback
                
    def getAdjacentTile(self, direction):
        """ Returns the adjacent tile in the given direction """
        if direction in self.tile.connections:
            return self.tile.connections[self.movementDelegate.direction]
        else:
            return None 
        
    def interactWithAdjacentTile(self):
        """ Interact with an adjacent city """
        destination = self.getAdjacentTile(self.movementDelegate.direction)
        if destination.contents is not None:
            destination.contents.interact(self.movementDelegate.direction)
            
    def interact(self, direction):
        """ Interact with the trainer """
        self.interactionDelegate.interact(direction)
                
    def performGameTick(self):
        """ Perform a single game tick """
        self.movementDelegate.performGameTick()
            
    def isBattleable(self):
        """ Return if the person is Battleable """
        return False 
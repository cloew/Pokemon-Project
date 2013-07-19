from Zone.direction import UP, DOWN, LEFT, RIGHT, GetTextFromDirection, GetOppositeDirection

class TrainerPositionWrapper:
    """ Wrapper for a Trainer that includes it's position in a zone """
    
    def __init__(self, trainer, tile, interactionCallback=None, message=None):
        """ Initialize the Trainer Position Wrapper """
        self.trainer = trainer
        self.tile = None
        self.setTile(tile)
        self.direction = DOWN
        
        self.moving = False
        self.moveTick = None
        
        self.message = message
        self.interactionCallback = interactionCallback
        
    def getImageBaseName(self):
        """ Return the base image name for the Trainer Position Wrapper """
        return "trainer_{0}".format(GetTextFromDirection(self.direction))
        
    def setTile(self, tile):
        """ Set the Trainer's current tile """
        if self.tile is not None:
            self.tile.setContents(None)
        self.tile = tile
        tile.setContents(self)
        
    def up(self):
        """ Move the Trainer up """
        self.prepareToMove(UP)
        
    def down(self):
        """ Move the Trainer down """
        self.prepareToMove(DOWN)
        
    def left(self):
        """ Move the Trainer left """
        self.prepareToMove(LEFT)
        
    def right(self):
        """ Move the Trainer right """
        self.prepareToMove(RIGHT)
        
    def stopMovingUp(self):
        """ Stop the Trainer from moving """
        self.stopMoving(UP)
        
    def stopMovingDown(self):
        """ Stop the Trainer from moving """
        self.stopMoving(DOWN)
        
    def stopMovingLeft(self):
        """ Stop the Trainer from moving """
        self.stopMoving(LEFT)
        
    def stopMovingRight(self):
        """ Stop the Trainer from moving """
        self.stopMoving(RIGHT)
            
    def stopMoving(self, direction):
        """ Stop Moving in the given direction """
        if self.direction is direction:
            self.moving = False
            self.moveTick = None
        
    def interactWithAdjacentTile(self):
        """ Interact with an adjacent city """
        destination = self.getAdjacentTile(self.direction)
        if destination.contents is not None:
            destination.contents.interact(self.direction)
            
    def interact(self, direction):
        """ Interact with the trainer """
        self.direction = GetOppositeDirection(direction)
        if self.interactionCallback is not None:
            self.interactionCallback(self, self.message)
        
    def prepareToMove(self, direction):
        """ Try to Move in the given direction """
        self.moving = True
        self.setMoveCoroutine()
        if direction is not self.direction:
            self.direction = direction
            
    def move(self, direction):
        """ Move in the given direction if possible """
        destination = self.getAdjacentTile(direction)
        if destination is not None:
            if destination.isEnterable():
                self.setTile(destination)
                
    def performGameTick(self):
        """ Perform a single game tick """
        if self.moving:
            self.moveTick.next()
            
    def setMoveCoroutine(self):
        """ Set the Move Coroutine """
        if self.moveTick is None:
            self.moveTick = self.moveCoroutine()
            self.moveTick.next()
        
    def moveCoroutine(self):
        """ Coroutine for moving """
        while True:
            for i in range(12):
                yield
            self.move(self.direction)
                
    def getAdjacentTile(self, direction):
        """ Returns the adjacent tile in the given direction """
        if direction in self.tile.connections:
            return self.tile.connections[direction]
        else:
            return None 
            
    def isBattleable(self):
        """ Return if the trainer is Battleable """
        return self.trainer.hasPokemon()
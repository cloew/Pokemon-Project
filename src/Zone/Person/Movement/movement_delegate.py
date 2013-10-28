from Zone.direction import UP, DOWN, LEFT, RIGHT, GetTextFromDirection, GetOppositeDirection

class MovementDelegate:
    """ Movement Delegate for a Zone Person """
    
    def __init__(self, parent, direction=DOWN):
        """ Initialize the Movement Delegate """ 
        self.parent = parent
        self.direction = direction
        self.newDirection = direction
        
        self.moving = False
        self.moveTick = None
        self.setMoveCoroutine()
    
    def prepareToMove(self, direction):
        """ Try to Move in the given direction """
        self.moving = True
        self.newDirection = direction
            
    def move(self, direction):
        """ Move in the given direction if possible """
        if self.direction != self.newDirection:
            self.direction = self.newDirection
        else:
            destination = self.getAdjacentTile(self.direction)
            if destination is not None:
                if destination.isEnterable():
                    self.parent.setTile(destination)
    
    def stopMoving(self, direction):
        """ Stop Moving in the given direction """
        if self.direction is direction:
            self.moving = False
            
    def setMoveCoroutine(self):
        """ Set the Move Coroutine """
        if self.moveTick is None:
            self.moveTick = self.moveCoroutine()
            self.moveTick.next()
        
    def moveCoroutine(self):
        """ Coroutine for moving """
        while True:
            if self.moving:
                self.move(self.direction)
                for i in range(12):
                    yield
            else:
                yield
                
    def getAdjacentTile(self, direction):
        """ Returns the adjacent tile in the given direction """
        if direction in self.parent.tile.connections:
            return self.parent.tile.connections[direction]
        else:
            return None 
                
    def performGameTick(self):
        """ Perform a single game tick """
        if self.moveTick is not None:
            self.moveTick.next()

def MakeMoveFunction(self, direction):
    def moveFunction():
        """ Move in the specified direction """
        self.movementDelegate.prepareToMove(direction)
    return moveFunction
    
def MakeStopMovingFunction(self, direction):
    def stopMovingFunction():
        """ Stop moving in the specified direction """
        self.movementDelegate.stopMoving(direction)
    return stopMovingFunction
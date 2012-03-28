from secondary_effect import SecondaryEffect

from Battle.FaintHandlers.faint_handler_factory import FaintHandlerFactory

class Mist(SecondaryEffect):
    """ Represents an extra effect that prevents stats from being lowered """
        
    def afterTurn(self, owner):
        """ Leech health from the owner and give it to the source """
        messages = [owner.getHeader() + self.message]
        
        messages += self.damage(owner)
        self.leech(owner)
        return messages
        
    def onStatMod(self, owner, degree, messages):
        """ Perform effect when owner is given a stat mod """
        if degree < 0:
            degree = 0
            addMessage(owner, messages)
        
        return degree
        
    def addMessage(self, owner, messages):
        """ Adds the message about mist if it is not already there """
        message = self.message % owner.getHeader()
        if not message in messages:
            messages.append(message)
from interaction_delegate import InteractionDelegate
from Zone.direction import GetDirectionFromText

from resources.tags import Tags

def LoadInteractionDelegateFromXML(contentElement):
    """ Load the Interaction Delegate """
    interactionElement = contentElement.find(Tags.interactionTag)
    if interactionElement is None:
        return None
        
    direction = interactionElement.findtext(Tags.directionTag)
    message = interactionElement.findtext(Tags.messageTag)
    
    return InteractionDelegate(message, direction=GetDirectionFromText(direction))
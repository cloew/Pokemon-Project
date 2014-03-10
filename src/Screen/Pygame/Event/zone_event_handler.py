from core_event_handler import PerformEvent as PerformCoreEvent

def PerformEvents(eventQueue, controller):
    """ Perform the given events """
    while len(eventQueue) > 0:
        event = eventQueue.popleft()
        PerformEvent(event, controller)
        
def PerformEvent(event, controller):
    """ Perform the given event """
    PerformCoreEvent(event, controller)
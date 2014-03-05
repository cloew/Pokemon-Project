from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController

def PerformEvents(eventQueue, controller):
    """ Perform the given events """
    while len(eventQueue) > 0:
        event = eventQueue.popleft()
        PerformEvent(event, controller)

def PerformEvent(event, controller):
    """ Perform the given event """
    controller.runController(MessageBoxController(event, controller.screen))
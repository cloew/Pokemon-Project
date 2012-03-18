from Battle.Status.status import Status

class Faint(Status):
    """ Represents a Faint Status for a Pokemon that has fainted """
    abbr = "FNT"
    start = " fainted."
    
    def __init__(self):
        """ Build a Status """
        self.initialize()
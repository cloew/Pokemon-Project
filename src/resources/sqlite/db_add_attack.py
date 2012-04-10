import sqlite3

class DBAddAttack:
    """ Adds an attack to the Database """
    def __init__(self):
        """  """
        self.commands = {'p':self.addParameters, 'h':self.addHit,
                                   'd':self.addDamage, 'c':self.addCrit, 's':self.addSpeed}
        self.vals = {'name':None, 'type':None}
    
    def execute(self, params):
        """  """
        for param in params:
            cmd = param[0]
            cmdParams = param[2:]
            
            self.commands[cmd](cmdParams)
            
    def addParameters(self, vals):
        """  """
        print vals
        
    def addHit(self, vals):
        """  """
        print vals
        
    def addDamage(self, vals):
        """  """
        print vals
        
    def addCrit(self, vals):
        """  """
        print vals
        
    def addSpeed(self, vals):
        """  """
        print vals
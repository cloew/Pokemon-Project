import sqlite3
from resources.sqlite.pokemon_sqlite_helper import PkmnDBConnect

from resources.sqlite.db_adder import DBAdder
from resources.sqlite.db_add_attack_in_use import DBAddAttackInUse

class DBAddPkmn(DBAdder):
    """ Adds a pkmn to the Database """
    def __init__(self), id, connection = None, cursor = None:
        """  """
        self.commands = {'a':self.addAttacks,
                                   'p':self.addParameters}
                                   
        self.vals = {'name':None,
                          'species_id':None,
                          'ability_id':None,
                          'level':None,
                          'currHP':None,
                          'trainer_id':id}
                          
        self.attacks = []
        
        self.trainer_id = id
        if connection is None:
            self.connection = PkmnDBConnect()
            self.cursor = self.connection.cursor()
        else:
            self.connection = connection
            self.cursor = cursor
    
    def execute(self, params, close = True):
        """  """
        for param in params:
            cmd = param[0]
            cmdParams = param[2:].split(':')
            
            self.commands[cmd](cmdParams)
            
        self.addSpecies()
            
        self.connection.commit()
        
        if (close):
            self.connection.close()
        
    def addPkmn(self):
        """ Adds the pkmn to the database """
        params = []
        toAdd = []
        
        for key in self.vals.keys():
            if self.vals[key] is None:
                continue
                
            params += [key]
            toAdd += [self.vals[key]]
            
        paramStr = self.GetStrFromList(params)
        
        print "Adding Pkmn:", self.vals['name']
        self.insertIntoDB("Pokemon", paramStr, toAdd)
        
        id = sself.cursor.lastrowid
        
        for attack in self.attacks:
            front = DBAddAttackInUse(id, connection = self.connection, cursor =  self.cursor)
            front.execute(attack)
            
    def addAttacks(self, vals):
        """ Adds Attacks parameters """
        self.attacks.append(vals)
    
    def addParameters(self, vals):
        """ Adds Species specific parameters """
        self.vals['name'] = vals[0]
        species = vals[1]
        self.vals['level'] = vals[2]
        self.vals['currHP'] = vals[3]
        
        
        self.cursor.execute("SELECT id from Species where species = ?", (species,))
        self.vals['species_id'] = self.cursor.fetchone()[0]
        
        print "Building Species:", self.vals['species']
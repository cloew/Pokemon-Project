import sqlite3
from resources.sqlite.pokemon_sqlite_helper import PkmnDBConnect

from resources.sqlite.db_adder import DBAdder

class DBAddSpecies(DBAdder):
    """ Adds a species to the Database """
    def __init__(self):
        """  """
        self.commands = {'a':self.addAbilities,
                                   'd':self.addDreamAbility,
                                   'p':self.addParameters,
                                   's':self.addStats,
                                   't':self.addTypes}
                                   
        self.vals = {'species':None,
                          'dex':None,
                          'HP':None,
                          'ATK':None,
                          'DEF':None,
                          'SPD':None,
                          'SATK':None,
                          'SDEF':None}
                          
        self.abilities = []
        self.types = []
        self.dreamAbilities = []
        
        self.connection = PkmnDBConnect()
        self.cursor = self.connection.cursor()
    
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
        
    def addSpecies(self):
        """ Adds the species to the database """
        params = []
        toAdd = []
        
        for key in self.vals.keys():
            if self.vals[key] is None:
                continue
                
            params += [key]
            toAdd += [self.vals[key]]
            
        paramStr = self.GetStrFromList(params)
        
        print "Adding Species:", self.vals['species']
        self.insertIntoDB("Species", paramStr, toAdd)
        
        self.cursor.execute("SELECT id from Species where species = ?", (self.vals['species'],))
        id = self.cursor.fetchone()[0]
        
        for type in self.types:
            self.insertIntoDB("SpeciesTypeJoin", "species_id, type_id", (id,)+(type,))
            
        for ability in self.abilities:
            self.insertIntoDB("SpeciesAbilityJoin", "species_id, ability_id", (id,)+(type,))
            
        for ability in self.dreamAbilities:
            self.insertIntoDB("SpeciesDreamAbilityJoin", "species_id, ability_id", (id,)+(type,))
            
    def addAbilities(self, vals):
        """ Adds Ability parameters """
        for ability in vals:
            if ability == "":
                continue
            ability = ability.strip()
            self.cursor.execute("SELECT id from Ability where name = ?", (ability,))
            self.abilities.append(self.cursor.fetchone()[0])
            
    def addDreamAbility(self, vals):
        """ Adds Dream Ability parameters """
        for dreamAbility in vals:
            dreamAbility = dreamAbility.strip()
            self.cursor.execute("SELECT id from Ability where name = ?", (dreamAbility,))
            self.dreamAbilities.append(self.cursor.fetchone()[0])
    
    def addParameters(self, vals):
        """ Adds Species specific parameters """
        self.vals['species'] = vals[0]
        self.vals['dex'] = vals[1]
        print "Building Species:", self.vals['species']
        
        self.checkForSpeciesAlready()
        
    def addStats(self, vals):
        """ Adds stats """
        self.vals['HP'] = vals[0]
        self.vals['ATK'] = vals[1]
        self.vals['DEF'] = vals[2]
        self.vals['SPD'] = vals[3]
        self.vals['SATK'] = vals[4]
        self.vals['SDEF'] = vals[5]
        
    def addTypes(self, vals):
        """ Adds types """
        for type in vals:
            type = type.strip()
            if type == "":
                continue
            
            self.cursor.execute("SELECT id from Type where name = ?", (type,))
            self.types.append(self.cursor.fetchone()[0])
        
    def checkForSpeciesAlready(self):
        """  """
        print "Checking for Species"
        self.cursor.execute("SELECT id from Species where species = ?", (self.vals['species'],))
        t = self.cursor.fetchone()
        
        if not t is None:
            print "Species %s already exists" % self.vals['species']
            raise Exception()
        print "Done checking Species"
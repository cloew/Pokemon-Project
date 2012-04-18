import sys
from resources.sqlite.db_add_ability import DBAddAbility
from resources.sqlite.db_add_attack import DBAddAttack
from resources.sqlite.db_add_species import DBAddSpecies

class DBFront:
    def __init__(self):
        self.commands = {"ADD ABILITY":DBAddAbility,
                                   "ADD ATTACK":DBAddAttack,
                                   "ADD SPECIES":DBAddSpecies}

    def GetStrFromList(self, args):
        """ Combines the cmd list into a single string """
        cmdStr = ""
        for message in args:
            if not cmdStr == "":
                cmdStr += " "
            cmdStr += message
            
        return cmdStr
        
    def GetCmdAndParams(self, cmdStr):
        """ Returns the Command Str and the Parameteres for the command """
        cmdAndParams = cmdStr.split("@")
        cmd = cmdAndParams[0].strip()
        params = cmdAndParams[1:]
        
        return cmd, params
        
    def executeCmd(self, args):
        """ Executes a command """
        cmdStr = self.GetStrFromList(args)
        cmd, params = self.GetCmdAndParams(cmdStr)
        front = self.commands[cmd]()
        front.execute(params)


def main(args):
    """ Takes the Command args and builds accordingly """
    front = DBFront()
    try:
        front.executeCmd(args)
    except Exception as e:
        print e
    
    
    
    


if __name__ == "__main__":
    main(sys.argv[1:])
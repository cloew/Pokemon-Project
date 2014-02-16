import sys
import os

import pbf.kao.pokemon.Commands

def IncludeLocalPBFCommands(ImportPythonDirectory):
    """ Import the local PBF Commands """
    localCommandsDirectory = os.path.join(os.path.dirname(__file__), "pbf/kao/pokemon/Commands")
    ImportPythonDirectory(localCommandsDirectory)

def ImportInstalledPBF():
    """ Modify System Path to ensure the Installed PBF Extensions are imported and available """
    module = sys.modules['pbf']
    del sys.modules['pbf']
    sys.path.remove(os.path.abspath('.'))

    import pbf
    from pbf.Commands import ImportPythonDirectory
    from pbf.Commands import command_manager as command_manager 

    sys.path.insert(0, os.path.abspath('.'))
    sys.modules['pbf'] = module
    
    return ImportPythonDirectory, command_manager

def main(args):
    """ Run the main file """
    ImportPythonDirectory, command_manager = ImportInstalledPBF()
    IncludeLocalPBFCommands(ImportPythonDirectory)
    command_manager.Run(args)

if __name__ == "__main__":
    main(sys.argv[1:])
from Battle.Actions.switch_action import SwitchAction
from InputProcessor import commands


from Menu.menu import Menu
from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry
from Screen.Console.Menu.PokemonMenu.pokemon_menu_screen import PokemonMenuScreen

from kao_console.ascii import ENDL, KAO_UP, KAO_DOWN, KAO_LEFT, KAO_RIGHT
from kao_gui.console.console_controller import ConsoleController

class SwitchController(ConsoleController):
    """ Controller for selecting a Battle Switch Action """
    
    def __init__(self, pokemon):
        """ Builds the Switch Controller """
        self.pokemon = pokemon
        self.action = None
        
        entries = []
        for pokemon in self.pokemon.getTrainer().beltPokemon:
            entries.append(PokemonMenuEntry(pokemon, self.setAction))
        self.menu = Menu(entries, columns=2)
        screen = PokemonMenuScreen(self.menu) # Need different screen

        cmds = {ENDL:self.menu.enter,
                KAO_UP:self.menu.up,
                KAO_DOWN:self.menu.down,
                KAO_RIGHT:self.menu.right,
                KAO_LEFT:self.menu.left}
                     
        ConsoleController.__init__(self, screen, commands=cmds, cancellable=True)
        
    def setAction(self, entry):
        """ Set the Chosen Action """
        if self.canSwitchTo(entry.getPokemon()):
            self.action = SwitchAction(self.pokemon, entry.getPokemon())
            self.stopRunning()
        else:
            """ Tell Screen to display message that the pokemon cannot be used """
            
    def canSwitchTo(self, newPokemon):
        """ Returns if the player can switch to the new Pokemon """
        return not self.pokemon.isPokemon(newPokemon)
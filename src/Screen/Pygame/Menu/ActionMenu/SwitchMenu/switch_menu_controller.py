from Battle.Actions.switch_action import SwitchAction
from InputProcessor import commands
from Menu.menu import Menu
from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.SwitchMenu.switch_menu_screen import SwitchMenuScreen

class SwitchMenuController(Controller):
    """ Controller for Switch Menu """
    
    def __init__(self, pokemon):
        """ Initialize the Switch Menu """
        Controller.__init__(self)
        self.pokemon = pokemon
        self.action = None
        
        entries = []
        for pokemon in self.pokemon.getTrainer().beltPokemon:
            entries.append(PokemonMenuEntry(pokemon, self.setAction))
        self.menu = Menu(entries, columns=2)
        
        self.screen = SwitchMenuScreen(self.menu)
        self.cmds = {commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.LEFT:self.menu.left,
                     commands.RIGHT:self.menu.right,
                     commands.SELECT:self.menu.enter,
                     commands.EXIT:self.stopRunning}
                     
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
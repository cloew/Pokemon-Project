from Battle.Actions.switch_action import SwitchAction
from InputProcessor import commands
from Menu.menu import Menu
from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry
from Screen.Pygame.Menu.ActionMenu.SwitchMenu.switch_menu_screen import SwitchMenuScreen

from kao_gui.pygame.pygame_controller import PygameController

class SwitchMenuController(PygameController):
    """ Controller for Switch Menu """
    
    def __init__(self, pokemon, cancellable=True):
        """ Initialize the Switch Menu """
        self.pokemon = pokemon
        self.action = None
        
        entries = []
        for pokemon in self.pokemon.getTrainer().beltPokemon:
            entries.append(PokemonMenuEntry(pokemon, self.setAction))
        self.menu = Menu(entries, columns=2)
        
        screen = SwitchMenuScreen(self.menu)
        cmds = {commands.UP:self.menu.up,
                commands.DOWN:self.menu.down,
                commands.LEFT:self.menu.left,
                commands.RIGHT:self.menu.right,
                commands.SELECT:self.menu.enter}
        if cancellable:
            cmds[commands.EXIT] = self.stopRunning
                
        PygameController.__init__(self, screen, commands=cmds)
                     
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
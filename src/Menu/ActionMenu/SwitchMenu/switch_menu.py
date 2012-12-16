from Menu.box_menu import BoxMenu
from pokemon_menu_entry import PokemonMenuEntry

from Battle.Actions.switch_action import SwitchAction

class SwitchMenu(BoxMenu):
    """ Represents the Battle's Switch Menu """

    def __init__(self, userPkmn):
        """ Create the Action Menu for the given Pokemon """
        self.pkmn = userPkmn
        self.action = None
        BoxMenu.__init__(self)
    
    def addEntries(self):
        """ Add Menu Entries """
        self.entries = []
        for pkmn in self.pkmn.getTrainer().beltPokemon:
            self.entries.append(PokemonMenuEntry(pkmn, self.setSwitchAction))

    def setSwitchAction(self, entry):
        """ Set the Switch Action """
        if not self.pkmn.isPokemon(entry.getPokemon()):
            self.action = SwitchAction(self.pkmn, entry.getPokemon())
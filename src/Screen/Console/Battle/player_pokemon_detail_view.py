# from Screen.Console.view import View
from Screen.Console.HealthBar.health_bar_view import HealthBarView

from kao_gui.console.console_widget import ConsoleWidget

class PlayerPokemonDetailView(ConsoleWidget):
    """ View for a Player's Pokemon's Details """

    def __init__(self, pokemon):
        """ Builds the Player's Pokemon Detail View """
        self.pokemon = pokemon
        self.healthBar = HealthBarView(pokemon.original)

    def draw(self):
        """ Returns the health bar as a console line """
        self.healthBar = HealthBarView(self.pokemon.original)
        return self.getEntryLines()

    def getEntryLines(self):
        """ Return entry lines """
        lines = []

        lines.append("")
        lines.append(self.getPokemonNameLine())
        lines.append(self.getHealthLine())
        lines.append(self.getHealthBarLine())
        lines.append("")
        return lines

    def getPokemonNameLine(self, ):
        """ Returns the Pokemon Name and Species as a string """
        name = self.getFullString(self.pokemon.getName())
        species = self.getFullString(self.pokemon.getSpecies())
        nameString = "{0} --- {1}".format(name, species)
        return self.getLine(nameString)

    def getHealthLine(self):
        """ Return the line with health stats """
        pkmn = self.pokemon
        return self.getLine("{0}/{1}".format(pkmn.getCurrHP(), pkmn.getStat("HP")))

    def getHealthBarLine(self):
        """ Return the line with health bar """
        healthBarText = self.healthBar.draw(self.terminal.width, False)
        return "{0}".format(healthBarText)

    def getFullString(self, string):
        """ Returns a string with the full 10 char limit """
        return (string + " "*10)[:10]

    def getLine(self, text):
        """ Returns a line """
        width = self.terminal.width
        spacerLeft = self.getLeftSpacerString(len(text), width)
        spacerRight = self.getRightSpacerString(len(spacerLeft), width)

        return "{0}{1}{2}".format(spacerLeft, text, spacerRight)

    def getLeftSpacerString(self, text_size, width):
        """ Returns the left spacer string """
        spacerSize = (width - text_size)/2
        return " "*spacerSize

    def getRightSpacerString(self, text_size, width):
        """ Returns the right spacer string """
        spacerSize = width - text_size
        return " "*spacerSize
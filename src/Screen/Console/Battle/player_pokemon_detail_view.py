from Screen.Console.view import View
from Screen.Console.HealthBar.health_bar_view import HealthBarView

class PlayerPokemonDetailView(View):
    """ View for a Player's Pokemon's Details """

    def __init__(self, pokemon):
        """ Builds the Player's Pokemon Detail View """
        self.pokemon = pokemon
        self.healthBar = HealthBarView(pokemon.original)

    def draw(self, window):
        """ Returns the health bar as a console line """
        return self.getEntryLines(window)

    def getEntryLines(self, window):
        """ Return entry lines """
        lines = []

        lines.append("")
        lines.append(self.getPokemonNameLine(window))
        lines.append(self.getHealthLine(window))
        lines.append(self.getHealthBarLine(window))
        lines.append("")
        return lines

    def getPokemonNameLine(self, window):
        """ Returns the Pokemon Name and Species as a string """
        name = self.getFullString(self.pokemon.getName())
        species = self.getFullString(self.pokemon.getSpecies())
        nameString = "{0} --- {1}".format(name, species)
        return self.getLine(nameString, window)

    def getHealthLine(self, window):
        """ Return the line with health stats """
        pkmn = self.pokemon
        return self.getLine("{0}/{1}".format(pkmn.getCurrHP(), pkmn.getStat("HP")), window)

    def getHealthBarLine(self, window):
        """ Return the line with health bar """
        healthBarText = self.healthBar.draw(window, window.terminal.width, False)
        return "{0}".format(healthBarText)

    def getFullString(self, string):
        """ Returns a string with the full 10 char limit """
        return (string + " "*10)[:10]

    def getLine(self, text, window):
        """ Returns a line """
        width = window.terminal.width
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
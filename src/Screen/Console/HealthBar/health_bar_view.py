from Screen.Console.view import View

class HealthBarView(View):
    """ Class to represent the view of a Pokemon's Health Bar """

    def __init__(self, pokemon):
        """ Builds the Health Bar View from the given Pokemon """
        self.pokemon = pokemon

    def draw(self, window, size):
        """ Returns the health bar as a console line """
        return "{0}{1}{2}".format(self.getHealthBarColor(window), "="*size, window.terminal.normal)

    def getHealthBarColor(self, window):
        """ Returns the Health Bar's color """
        healthPercentage = self.pokemon.getCurrHP()*100/self.pokemon.getStat("HP")
        color = ""
        if healthPercentage > 50:
            color = window.terminal.green
        elif healthPercentage > 25:
            color = window.terminal.yellow
        else:
            color = window.terminal.red
        return color
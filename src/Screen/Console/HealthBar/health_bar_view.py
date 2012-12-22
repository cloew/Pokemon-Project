from Screen.Console.view import View

class HealthBarView(View):
    """ Class to represent the view of a Pokemon's Health Bar """

    def __init__(self, pokemon):
        """ Builds the Health Bar View from the given Pokemon """
        self.pokemon = pokemon

    def draw(self, window, size):
        """ Returns the health bar as a console line """
        return "{t.reverse}{0}{1}{t.normal}".format(self.getHealthBarColor(window), " "*size, t=window.terminal)

    def getHealthBarColor(self, window):
        """ Returns the Health Bar's color """
        healthPercentage = self.pokemon.getCurrHP()*100/self.pokemon.getStat("HP")
        colors = [window.terminal.green,
                  window.terminal.yellow,
                  window.terminal.red]

        color = ""
        if healthPercentage > 50:
            color = colors[0]
        elif healthPercentage > 25:
            color = colors[1]
        else:
            color = colors[2]
        return color
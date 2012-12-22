from Screen.Console.view import View

class HealthBarView(View):
    """ Class to represent the view of a Pokemon's Health Bar """

    def __init__(self, pokemon):
        """ Builds the Health Bar View from the given Pokemon """
        self.pokemon = pokemon

    def draw(self, window, size):
        """ Returns the health bar as a console line """
        return self.getHealthBarText(size).format(self.getHealthBarColor(window), t=window.terminal)

    def getHealthBarText(self, size):
        """ Returns the health bar string """
        healthPercentage = self.getHealthPercentage()
        healthBarSpaces = " "*int(size*healthPercentage/100)
        healthSpaces = " "*(size-len(healthBarSpaces))
        return "{t.reverse}{0}" + healthBarSpaces + "{t.normal}" + healthSpaces

    def getHealthBarColor(self, window):
        """ Returns the Health Bar's color """
        healthPercentage = self.getHealthPercentage()
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

    def getHealthPercentage(self):
        """ Returns the percentage of the Pokemon's health """
        return (self.pokemon.getCurrHP()*100)/self.pokemon.getStat("HP")
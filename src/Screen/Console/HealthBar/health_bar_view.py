from Screen.Console.view import View

from kao_gui.console.console_widget import ConsoleWidget

class HealthBarView(ConsoleWidget):
    """ Class to represent the view of a Pokemon's Health Bar """

    def __init__(self, pokemon):
        """ Builds the Health Bar View from the given Pokemon """
        self.pokemon = pokemon

    def draw(self, size, selected):
        """ Returns the health bar as a console line """
        format = ""
        if selected:
            format = self.terminal.reverse

        return self.getHealthBarText(size).format(self.getHealthBarColor(), format, t=self.terminal)

    def getHealthBarText(self, size):
        """ Returns the health bar string """
        healthPercentage = self.getHealthPercentage()
        healthBarSpaces = " "*int(size*healthPercentage/100)
        healthSpaces = " "*(size-len(healthBarSpaces))
        return "{t.reverse}{0}" + healthBarSpaces + "{t.normal}{1}" + healthSpaces + "{t.normal}"

    def getHealthBarColor(self):
        """ Returns the Health Bar's color """
        healthPercentage = self.getHealthPercentage()
        colors = [self.terminal.green,
                  self.terminal.yellow,
                  self.terminal.red]

        color = ""
        if healthPercentage > 50:
            color = colors[0]
        elif healthPercentage > 10:
            color = colors[1]
        else:
            color = colors[2]
        return color

    def getHealthPercentage(self):
        """ Returns the percentage of the Pokemon's health """
        return (self.pokemon.getCurrHP()*100)/self.pokemon.getStat("HP")
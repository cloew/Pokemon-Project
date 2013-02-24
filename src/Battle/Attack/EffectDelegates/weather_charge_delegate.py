from charge_delegate import ChargeDelegate

class WeatherChargeDelegate(ChargeDelegate):
    """ Represents a charge effect that does not need to charge in certain weather """
    
    def __init__(self, turns, turnToAttack, message, weatherType):
        """ Builds a Weather Charge Delegate """
        self.weatherType = weatherType
        ChargeDelegate.__init__(self, turns, turnToAttack, message)
    
    def isCharging(self, user, environment):
        """ Determines if the attack should not be completed because it is charging """
        self.getTurns(environment)
        if environment.weather.type == self.weatherType:
            self.turnOn = self.turnToAttack
        return ChargeDelegate.isCharging(self, user, environment)
        
    def getTurns(self, environment):
        """ Get the number of turns to charge for """
        if environment.weather.type == "RAIN": # Hard-coded for Solar Beam currently
            self.turns = 3
            self.turnToAttack = 2
        else:
            self.turns = 2
            self.turnToAttack = 1
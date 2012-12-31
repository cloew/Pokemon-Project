from charge_delegate import ChargeDelegate

class WeatherChargeDelegate(ChargeDelegate):
    """ Represents a charge effect that does not need to charge in certain weather """
    
    def __init__(self, turns, turnToAttack, message, weatherType):
        """ Builds a Weather Charge Delegate """
        self.weatherType = weatherType
        ChargeDelegate.__init__(self, turns, turnToAttack, message)
    
    def isCharging(self, user, environment):
        """ Determines if the attack should not be completed because it is charging """
        if environment.weather.type == self.weatherType:
            self.turnOn = self.turnToAttack
        return ChargeDelegate.isCharging(self, user)
    
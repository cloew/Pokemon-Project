from erratic_experience_rate import ErraticExperienceRate
from fast_experience_rate import FastExperienceRate
from fluctuating_experience_rate import FluctuatingExperienceRate
from medium_fast_experience_rate import MediumFastExperienceRate
from medium_slow_experience_rate import MediumSlowExperienceRate
from slow_experience_rate import SlowExperienceRate

ERRATIC = "ERRATIC"
FAST = "FAST"
FLUCTUATING = "FLUCTUATING"
MEDIUM_FAST = "MEDIUM FAST"
MEDIUM_SLOW = "MEDIUM SLOW"
SLOW = "SLOW"

stringToRate = {ERRATIC:ErraticExperienceRate,
                FAST:FastExperienceRate,
                FLUCTUATING:FluctuatingExperienceRate,
                MEDIUM_FAST:MediumFastExperienceRate,
                MEDIUM_SLOW:MediumSlowExperienceRate,
                SLOW:SlowExperienceRate}
                
def buildExperienceRate(rateType):
    """ Return the Experience Rate for the given type """
    global stringToRate
    if rateType not in stringToRate:
        print "Unable to find Experience Rate:", rateType
        exit(-2)
    return stringToRate[rateType]()
from affect_user_faint import AffectUserFaintDelegate
from either_faint import EitherFaintDelegate
from faint_handler import FaintHandlerDelegate
from target_faint import TargetFaintDelegate
from user_faint import UserFaintDelegate

class FaintHandlerFactory:
    """ Factory for Faint Handler Delegates """
    AFFECT_USER = "AFFECT USER"
    EITHER = "EITHER"
    REGULAR = "REGULAR"
    TARGET = "TARGET"
    USER = "USER"
    
    
    faintHandlers = {AFFECT_USER:AffectUserFaintDelegate,
                            EITHER:EitherFaintDelegate,
                            REGULAR:FaintHandlerDelegate,
                            TARGET:TargetFaintDelegate,
                            USER:UserFaintDelegate}
    
    @staticmethod
    def buildFromType(type):
        """ Builds a Faint Handler Delegate from the Type """
        return FaintHandlerFactory.faintHandlers[type]()
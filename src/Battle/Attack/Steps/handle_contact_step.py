from Battle.Attack.Steps.attack_step import AttackStep

class HandleContactStep(AttackStep):
    """ Represents the Handling Contact Step of the Attack Process """
    
    def perform(self, user, target, environment):
        """ Perform this step """
        messages = []
        
        if self.parent.makes_contact:
            messages += target.getAbility().onContact(target, user)
        return messages
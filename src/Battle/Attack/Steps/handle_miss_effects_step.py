from Battle.Attack.Steps.attack_step import AttackStep

class HandleMissEffectsStep(AttackStep):
    """ Represents the Handle Miss Effects in the Attack Process """
    
    def perform(self, user, target, environment):
        """ Perform this step """
        messages = []
        for effect in self.parent.effectDelegates:
            if hasattr(effect, "applyOnMiss"):
                effectMessages = effect.applyEffect(user, target, environment)
                messages = messages + effectMessages
            if hasattr(effect, "effectOnMiss"):
                effectMessages = effect.effectOnMiss(user, target, environment)
                messages = messages + effectMessages
        return messages
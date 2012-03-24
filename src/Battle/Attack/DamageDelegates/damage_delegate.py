from Battle.Attack.DamageDelegates.effectiveness import Effectiveness

import random 

class DamageDelegate(object):
    """ Handles how an Attack deals Damage """
    statLevels = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    
    def __init__(self, parent, power, isPhysical):
        """ """
        self.parent = parent
        self.power = power
        self.isPhysical = isPhysical
    
    def doDamage(self, user, target):
        """ Calculates the damage the attack does
        Returns the damage done """
        messages = []
    
        # Apply the modifier, have the target take damage
        damage, messages = self.damage(user, target)
        messages += self.takeDamage(damage, target)
        
        # Return the messages
        return messages
        
    def damage(self, user, target):
        """ Returns  the damage of the attack
        including effectiveness and STAB """
        messages = []
        
        # Get damage
        damage = self.calcDamage(user, target)
        
        # Get modifiers
        mod = self.getEffectiveness(messages, target)
        mod = mod*self.getStab(user)
        mod = mod*self.getCrit(messages, user, target)
        
        return self.normalize(damage*mod, target), messages
        
    def calcDamage(self, user, target):
        """ Calculate the damage before modifiers """
        return self.coreDamage(user, target)*self.applyRand()
        
    def coreDamage(self, user, target):
        """ Calculate the damage before modifiers and rands """
        atkStat, defStat = self.getAtkAndDefType()
    
        attack = self.getStatWithMod(atkStat, user)
        defense = self.getStatWithMod(defStat, target)
        level = user.getLevel()
        
        power = self.getPower(user, target)
        
        return ((((2*level/5 + 2)*attack*power/defense)/50) + 2)
        
    def getPower(self, user, target):
        """ Returns the power of the move """
        return self.power
        
    def getAtkAndDefType(self):
        """ Returns the stat that should be used for attack and defense """
        if self.isPhysical:
            return "ATK", "DEF"
        else:
            return "SATK", "SDEF"
        
    def getStatWithMod(self, stat, pkmn):
        """ Returns the sepcified stat, modified by the pkmn's stat mods """
        result = pkmn.getStat(stat)
        modLevel = pkmn.statMods[stat]
        mod = DamageDelegate.statLevels[abs(modLevel)]
        
        if modLevel < 0:
            mod = 1/mod
        return result*mod
        
    def applyRand(self):
        return random.randint(85, 100)/100.0
        
    def normalize(self, damage, target):
        """ Damage cannot be lower than 1, unless the target is immune """
        if damage == 0:
            return 0
        elif damage < 1:
            return 1
        elif damage > target.getCurrHP():
            return target.getCurrHP()
        return int(damage)
        
    def getEffectiveness(self, messages, target):
        """ Returns the modifier returned based on effectiveness
        and adds the message to the list of messages """
        mod, message = Effectiveness.getEffectiveness(self.parent.type,\
                target.getTypes())
    
        if message:
            messages.append(message)
            
        return mod
        
    def getStab(self, user):
        """ Returns the modifier for STAB """
        if self.parent.type in user.getTypes():
            return user.getAbility().onStab()
        return 1
        
    def getCrit(self, messages, user, target):
        """ Returns whether crit worked """
        newMod = 1
        if hasattr(self.parent, "critDelegate"):
            crit, message = self.parent.critDelegate.crit(user)
            if crit:
                newMod = user.getAbility().giveCrit(2)
                newMod, abilityMessages = target.getAbility().takeCrit\
                                                                        (newMod, target, user)
                
                if newMod > 1:
                    messages.append(message)
                    for message in abilityMessages:
                        messages.append(message)
                    
        return newMod
        
    def takeDamage(self, damage, target):
        """ Has the target take damage """
        return target.takeDamage(damage)
        
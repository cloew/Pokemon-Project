from Battle.Attack.Steps.attack_step import AttackStep

class AnnouncementStep(AttackStep):
    """ Represents the Announcement Step in the Attack Process """
    
    def perform(self, user, target, environment):
        """ Perform this step """
        return ["%s USED %s" % (user.getHeader(), self.parent.name)]
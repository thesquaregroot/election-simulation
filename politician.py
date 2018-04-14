import statistics
import math

class Politician:
    def __init__(self, name, economicFactor, socialFactor):
        self.name = name
        self.trueEconomicFactor = economicFactor
        self.trueSocialFactor = socialFactor
        self.publicEconomicFactor = economicFactor
        self.publicSocialFactor = socialFactor

    def campaign(self, competition, citizens):
        # Do nothing.
        #
        # This is effectively an "honest" politician
        # who doesn't change their public views in response to the populace
        #
        # Other politician types can override this method to update their
        # public views based on the views of their constituents or competitors
        return

class FollowTheCenterPolitician(Politician):

    def campaign(self, competition, citizens):
        # try to move closer to the median citizen viewpoint
        centerEconomicPosition = statistics.median(c.economicFactor for c in citizens)
        centerSocialPosition = statistics.median(c.socialFactor for c in citizens)
        centerVector = [centerEconomicPosition - self.publicEconomicFactor, centerSocialPosition - self.publicSocialFactor]
        correctionVector = centerVector
        # but stay away from opponents, but in less magnitude than our correction
        avoidanceFactor = 0.5 * math.sqrt(centerVector[0]**2 + centerVector[1]**2)
        for opponent in competition:
            opponentEconomicCorrection = avoidanceFactor * (opponent.trueEconomicFactor - self.trueEconomicFactor)
            opponentSocialCorrection   = avoidanceFactor * (opponent.trueSocialFactor - self.trueSocialFactor)
            correctionVector[0] -= opponentEconomicCorrection
            correctionVector[1] -= opponentSocialCorrection
        # apply correction vector to public views
        self.publicEconomicFactor += correctionVector[0]
        self.publicSocialFactor += correctionVector[1]


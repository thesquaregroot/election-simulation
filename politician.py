import statistics
import math

class Politician:
    def __init__(self, name, economicPosition, socialPosition):
        self.name = name
        self.trueEconomicPosition = economicPosition
        self.trueSocialPosition = socialPosition
        self.publicEconomicPosition = economicPosition
        self.publicSocialPosition = socialPosition

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
        centerEconomicPosition = statistics.median(c.economicPosition for c in citizens)
        centerSocialPosition = statistics.median(c.socialPosition for c in citizens)
        centerVector = [centerEconomicPosition - self.publicEconomicPosition, centerSocialPosition - self.publicSocialPosition]
        correctionVector = centerVector
        # but stay away from opponents, but in less magnitude than our correction
        centerCorrectionLength = math.sqrt(centerVector[0]**2 + centerVector[1]**2)
        avoidanceFactor = 1 / (len(competition) + 1)
        for opponent in competition:
            economicDifference = opponent.trueEconomicPosition - self.trueEconomicPosition
            socialDifference   = opponent.trueSocialPosition - self.trueSocialPosition
            # normalize avoidance to the size of the center correction
            opponentDifferenceLength = math.sqrt(economicDifference**2 + socialDifference**2)
            normalizationFactor = centerCorrectionLength / opponentDifferenceLength
            # incorporate opponent correction into position
            opponentEconomicCorrection = avoidanceFactor * normalizationFactor * economicDifference
            opponentSocialCorrection   = avoidanceFactor * normalizationFactor * socialDifference
            correctionVector[0] -= opponentEconomicCorrection
            correctionVector[1] -= opponentSocialCorrection
        # apply correction vector to public views
        self.publicEconomicPosition += correctionVector[0]
        self.publicSocialPosition += correctionVector[1]


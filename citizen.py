import math

class Citizen:
    def __init__(self, economicPosition, socialPosition):
        self.economicPosition = economicPosition
        self.socialPosition = socialPosition

    def vote(self, politicians):
        vote = (0, None)
        for politician in politicians:
            score = self._score(politician)
            if score > vote[0]:
                vote = (score, politician.name)
        # return the politician the citizen is voting for
        # this can be None (no vote) if score for all politicians is less than 0
        return vote[1]

    def _score(self, politician):
        economicDifference = politician.publicEconomicPosition - self.economicPosition
        socialDifference = politician.publicSocialPosition - self.socialPosition

        difference = math.sqrt(economicDifference**2 + socialDifference**2)

        score = 1 - difference
        # this can go negative since the diagonal distance across the whole grid is 2*sqrt(2) = 2.828...
        #
        # a positive score indicates that the citizen would vote for this candidate if they have the highest score
        # a negative score indicates that the citizen would never vote for this candidate, even if they have the highest score
        return score


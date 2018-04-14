
class Campaign:
    def __init__(self):
        self.politicians = []
        self.citizens = []
        self.duration = 1
    
    def simulate(self):
        phase = 0
        while phase < self.duration:
            self._updatePoliticians()
            yield self._vote()
            phase += 1

    def _updatePoliticians(self):
        for politician in self.politicians:
            competition = self._getCompetition(politician)
            politician.campaign(competition, self.citizens)

    def _getCompetition(self, politician):
        competition = list(self.politicians)
        competition.remove(politician)
        return competition

    def _vote(self):
        votes = {}
        for citizen in self.citizens:
            vote = citizen.vote(self.politicians)
            if vote is not None:
                if vote in votes:
                    votes[vote] += 1
                else:
                    votes[vote] = 1
        return votes


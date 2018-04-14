
from campaign import *
from politician import *
from citizen import *

import random

def printPoliticianStates(campaign):
    for politician in campaign.politicians:
        print('\t%s: %6.3f, %6.3f' % (politician.name, politician.publicEconomicFactor, politician.publicSocialFactor))

if __name__ == "__main__":
    campaign = Campaign()
    campaign.politicians = [Politician('P1', 0.0, 0.0), FollowTheCenterPolitician('P2', 0.5, 0.5)]
    for i in range(100000):
        economicFactor = random.normalvariate(0.0, 0.1)
        socialFactor = random.normalvariate(0.0, 0.1)
        campaign.citizens.append(Citizen(economicFactor, socialFactor))
    campaign.duration = 5
    phase = 1
    printPoliticianStates(campaign)
    for results in campaign.simulate():
        winner = None
        winningVotes = 0
        for politician in results:
            if results[politician] > winningVotes:
                winner = politician
                winningVotes = results[politician]
        state = 'won!' if phase == campaign.duration else 'is ahead.'
        print(results, ': ', winner, state)
        printPoliticianStates(campaign)
        phase += 1


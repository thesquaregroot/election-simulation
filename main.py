
from campaign import *
from politician import *
from citizen import *
from visualizer import *

import random
import math

def printResults(phase, campaign, results):
    winner = None
    winningVotes = 0
    for politician in results:
        if results[politician] > winningVotes:
            winner = politician
            winningVotes = results[politician]
    state = 'won!' if phase == campaign.duration else 'is ahead.'
    voteWidth = int(math.log10(len(campaign.citizens)))
    print("Phase %d: %s %s" % (phase, winner, state))
    for politician in campaign.politicians:
        votes = results[politician.name]
        outputFormat = '%s received %' + str(voteWidth) + 'd votes (%6.3f, %6.3f)'
        print(outputFormat % (politician.name, votes, politician.publicEconomicPosition, politician.publicSocialPosition))
    print()

def printPoliticianStates(campaign):
    print("Initial State:")
    for politician in campaign.politicians:
        print('%s: %6.3f, %6.3f' % (politician.name, politician.trueEconomicPosition, politician.trueSocialPosition))
    print()

if __name__ == "__main__":
    campaign = Campaign()
    campaign.politicians = [Politician('P1', 0.0, 0.0), FollowTheCenterPolitician('P2', 0.5, 0.5), FollowTheCenterPolitician('P3', -0.1, -0.5)]
    for i in range(10000):
        economicPosition = random.normalvariate(0.05, 0.1)
        socialPosition = random.normalvariate(0.00, 0.1)
        campaign.citizens.append(Citizen(economicPosition, socialPosition))
    campaign.duration = 5
    phase = 1
    printPoliticianStates(campaign)
    visualizer = Visualizer(campaign)
    for results in campaign.simulate():
        printResults(phase, campaign, results)
        visualizer.addResults(results)
        phase += 1
    visualizer.waitUntilClosed()


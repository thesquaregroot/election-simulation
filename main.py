
from campaign import *
from politician import *
from citizen import *
from visualizer import *

import random

def printResults(campaign, results):
    winner = None
    winningVotes = 0
    for politician in results:
        if results[politician] > winningVotes:
            winner = politician
            winningVotes = results[politician]
    state = 'won!' if phase == campaign.duration else 'is ahead.'
    for politician in sorted(results):
        print('%s received %d votes' % (politician, results[politician]))
    print(winner, state)

def printPoliticianStates(campaign):
    for politician in campaign.politicians:
        print('\t%s: %6.3f, %6.3f' % (politician.name, politician.publicEconomicPosition, politician.publicSocialPosition))

if __name__ == "__main__":
    campaign = Campaign()
    campaign.politicians = [Politician('P1', 0.0, 0.0), FollowTheCenterPolitician('P2', 0.5, 0.5), FollowTheCenterPolitician('P3', -0.1, -0.5)]
    for i in range(100000):
        economicPosition = random.normalvariate(0.05, 0.1)
        socialPosition = random.normalvariate(0.00, 0.1)
        campaign.citizens.append(Citizen(economicPosition, socialPosition))
    campaign.duration = 5
    phase = 1
    printPoliticianStates(campaign)
    visualizer = Visualizer(campaign)
    for results in campaign.simulate():
        printResults(campaign, results)
        printPoliticianStates(campaign)
        visualizer.addResults(results)
        phase += 1
    visualizer.waitUntilClosed()


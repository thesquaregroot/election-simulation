import matplotlib.pyplot as plot

class Visualizer:
    def __init__(self, campaign):
        self.campaign = campaign
        # add citizens to plot immediately
        citizenPoints = [ (c.economicPosition, c.socialPosition) for c in campaign.citizens ]
        citizenX = [ p[0] for p in citizenPoints ]
        citizenY = [ p[1] for p in citizenPoints ]
        plot.ion()
        plot.scatter(citizenX, citizenY)
        plot.xlim(-1, 1)
        plot.ylim(-1, 1)
        plot.pause(0.01) # allows plot to refresh

    def addResults(self, results):
        politicianPoints = []
        for politician in self.campaign.politicians:
            # TODO: display number of votes
            politicianPoints.append((politician.publicEconomicPosition, politician.publicSocialPosition))
        politicianX = [ p[0] for p in politicianPoints ]
        politicianY = [ p[1] for p in politicianPoints ]
        plot.scatter(politicianX, politicianY, c='r')
        plot.pause(0.01) # allows plot to refresh

    def waitUntilClosed(self):
        plot.show(block=True)


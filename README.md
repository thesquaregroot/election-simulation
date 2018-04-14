# election-simulation
This project provide components that be used to create agent-based simulations
of elections.

With different politician and citizen implementations this project could be
used to analyze the effects of different campaigning strategies and their
effectiveness in different populations.  Political views are expressed as a
two-dimensional model, with economic and social axes each ranging from -1 to 1.

Campaign objects model elections and the lead-up to them by "polling" the
citizens and providing the politicians an opportunity to "campaign" by
modifying their public position.  The final phase of a campaign is the election
itself. Any number of citizens can be added to a campaign and are not required
to vote (e.g. if there are no candidates they like enough or if the candidates
are sufficiently similar).

The `main.py` file contains an example simulation that can modified are used as
an illustration of how to build others.


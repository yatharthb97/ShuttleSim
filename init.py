## Coarse grained simulation of Badminton Dynamics


"""
Todo:
1. Finish documentation
2. Update terminology in ubiquitious language document
3. Change Position.rand_positions() to a pure numpy function
"""





class Shuttle:

	def __init__(self):
		self.pos = ShuttlePosition()
		self.last_team = self.pos.team_ss[0]

	# For Completeness only ↓
	def toggle(self):
		"""	
		Activity state of Shuttle is toggled.
		"""
		self.last_team = self.pos.team
		self.pos.team = not self.pos.team

	def maintain(self):
		"""
		Activity state of Shuttle is maintained.
		"""
		self.last_team = self.pos.team

	def activity(self):
		return self.pos.team==self.last_team









def func(x):
	return x*0.99











class Court:


	sites = [0, 1, 2, 3]

	def __init__():
		

		self.side0 = [ Player(side=0, team_id=0, ability=0.5),
					   Player(side=0, team_id=1, ability=0.5)]

		self.side1 = [ Player(side=1, team_id=0, ability=0.5),
					   Player(side=1, team_id=1, ability=0.5) ] 
		# Index of list does not reflect actual position of player
		self.sides = [self.side0, self.side1]
		self.score = [0, 0] # Score of both the teams

		self.shuttle = Shuttle()


		def evolve(time_steps):
			"""
			function that evolves the game
			"""

			# Select Service Side
			playerA = Rule.serve()
			playerB =Rule.serve_receiver()
			
			side = Rule.side_selector()
			side = not side # ugly TODO: Fix ugly
			# Treat Service as a shot 
			shuttle.in_play = True

			# Shuttle block
			while self.shuttle.in_play:
				"""
				Side is toggled until the shuttle is active.
				"""
				self.sides[not side][playerA].play(self.shuttle)
				playerB = Rnd.




class Rule:
	"""
	Collection of functions that take in `court pos`, `side pos`, `score`.

	Generates 
	"""

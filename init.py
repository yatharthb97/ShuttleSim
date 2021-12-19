## Coarse grained simulation of Badminton Dynamics


"""
Objects in study:
	• Game : A complete `n` point game (n=20)
	• Rally : One complete cycle of returns
	• 

→ Agents:
	• Shuttle : Represents a generic shuttle class
	• Player : Represents the palyer and racket which is assumed to be a common entity.
			   (Energy Source) defined by state space `Ability` and  `Position`.
	• 


Modules:
	• Rules : Set of functions that select the agents
"""

class Shuttle:

	pos_ss = [0, 1, 2, 3] # Position State Space
	activity_ss = [False, True] # Active or inactive

	def __init__(self):
		self.position = self.pos_ss[0] # Possible positions → [0, 1, 2, 3]

		self.activity = activity_ss[0]







	# For Completeness only ↓

	def toggle(self):
		"""	
		Activity state of Shuttle is toggled.
		"""
		score = 1 * self.activity
		self.activity = not self.activity
		return score

	def maintained(self):
		"""
		Activity state of Shuttle is maintained.
		"""
		return None


class Player:


	def __init__(self, side, team_id, ability=0.5):
		
		if side not in [0,1]:
			raise Exception("Invalid side given to player!")

		if tam_id not in [0,1]:
			raise Exception("Invalid team_id given to player!")

		self.ability = ability # Ability of the player (defined as float in [0, 1])
		self.misses = self.miss_ratio() # Fraction of shots missed

		self.court_pos_ss = [0,1] + side # State space in court position

		self.side_pos = team_id # Position of player (side coordinates)
		self.court_pos = side[team_id] # Position of player (court coordinates)




	def miss_ratio():
		"""
		Fraction of shots missed by the player. It is some function of the `ability` value.
		"""

		return 1 - self.ability




class Court:


	sites = [0, 1, 2, 3]

	def __init__():
		

		self.side0 = [ Player(side=0, team_id=0, ability=0.5),
					   Player(side=0, team_id=1, ability=0.5)]

		self.side1 = Player(side=1, team_id=0, ability=0.5),
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
			playerA = Rule.serve_selector()
			side = Rule.side_selector()
			side = not side # ugly TODO: Fix ugly
			# Treat Service as a shot 

			# Shuttle block
			while self.shuttle.is_active():
				"""
				Side is toggled until the shuttle is active.
				"""
				self.sides[not side][playerA].play(self.shuttle)
				playerB = Rule.player_selector()
				self.sides[not side][playerB]

				playerA = Rule.player_selector()



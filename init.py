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



• Coordinate system for side -> n X m matrix
• Write Rule class 

• 
"""



class Position:

	team_ss = (0, 1) # Team coordinate state space


	def __init__(self, team_id, x_len, y_len):
		
		self.team = team_id

		self.x_ss = np.arange(x_len)
		self.y_ss = np.arange(y_len)

		self.xy = np.array([self.x_ss[0], self.y_ss[0]]) # x & y coordinates

	def set_pos(self, x, y):
		self.xy[0] = x
		self.xy[1] = y


	def get_pos(self):
		return [self.team, *self.xy]

	def rand_positions(self, n=2):
		x_list = np.random.sample(self.x_ss, n)
		y_list = np.random.sample(self.y_ss, n)
		zipped = [list(pos) for pos in zip(x_list, y_list)]
		return zipped

	def is_valid(self):
		return (self.team in self.team_ss) and (self.xy[0] in self.x_ss) and (self.xy[1] in self.y_ss)

	def __repr__():
		return f"[[{self.team} - {self.xy} ]]"


class ShuttlePosition(Position):

	def __init__(self, team_id, x_len, y_len):
		super().__init__(team_id, x_len, y_len)

	def set_team(self, new_team):
		team = new_team



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



class Player:


	def __init__(self, side, team_id, ability=0.5):
		
		if side not in [0,1]:
			raise Exception("Invalid side given to player!")

		if team_id not in [0,1]:
			raise Exception("Invalid team_id given to player!")

		self.ability = ability # Ability of the player (defined as float in [0, 1])
		self.affinity = self.ability

		self.misses = self.miss_ratio() # Fraction of shots missed

		#self.court_pos_ss = [0,1] + side # State space in court position

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

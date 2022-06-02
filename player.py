




class Battery:


	def __init__(self, ability, rally_t_fn, shot_cost, move_cost):
		"""
		
		# rally_t_fn=lambda x, t: x - t*0.99
		"""
		self.ability = ability
		self.rally_t_fn = rally_t_fn

		self.affinity = ability

		self.shot_cost = shot_cost
		self.move_cost = move_cost

	def get_affinity(self, time, took_shot, movement):
		"""
		Scales the affinity and returns the updated affinity.
		"""

		# Rally time
		affinity = self.rally_t_fn(self.affinity, time.t_rally)

		# Shot time
		affinity = affinity - (took_shot * self.shot_cost)
		affinity = affinity - (movement * self.move_cost)

		self.affinity = affinity
		return affinity


class Player:


	def __init__(self, side, team_id, ability=0.5):
		
		if side not in [0,1]:
			raise Exception("Invalid side given to player!")

		if team_id not in [0,1]:
			raise Exception("Invalid team_id given to player!")

		self.skill = {"ability": 0.5} # Ability of the player (defined as float in [0, 1])
		self.affinity = self.ability

		self.misses = self.miss_ratio() # Fraction of shots missed

		#self.court_pos_ss = [0,1] + side # State space in court position

		self.side_pos = team_id # Position of player (side coordinates)
		self.court_pos = side[team_id] # Position of player (court coordinates)

		self.battery = Battery(self.skill["ability"])

	def miss_ratio():
		"""
		Fraction of shots missed by the player. It is some function of the `ability` value.
		"""

		return 1 - self.ability

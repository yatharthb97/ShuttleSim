



class Battery:

	"""
	It represents and manages any generic ability of a Player object.
	"""

	def __init__(self, rally_t_fn, shot_cost, move_cost, ability=0):
		"""
		
		# rally_t_fn=lambda x, t: x - t*0.99
		"""
		self.ability = ability
		self.rally_t_fn = rally_t_fn

		self.affinity = self.ability

		self.shot_cost = shot_cost
		self.move_cost = move_cost

	def set_ability(self, value):
		self.ability = value
		self.affinity = value

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

	def charge(self):
		return self.affinity

	def restart(self):
		self.affinity = self.ability

	def __repr__(self):
		return f"Battery - Shot#{self.shot_cost} Move#{self.move_cost} ScaleFn#{self.rally_t_fn}"


	def SimpleBattery():
		#rally_t_fn, shot_cost, move_cost
		bat = Battery(lambda x : x, 0, 0)
		return bat

	def Battery1():
		#rally_t_fn, shot_cost, move_cost
		bat = Battery(lambda x: x*0.99, 0, 0.1)
		return bat



class Player:
	'''
	Attributes
	• unique Identifier
	• Coordinates
	• Skillset
	• Battery
	• Performance Metrics (optional)

	Actions
	• Moves
	• Hits Shots / Misses Shots
	• Drains energy
	'''
	idx_ = -1
	def gen_id():
		idx_ += 1
		return idx_

	def __init__(self, side, team_id, ability=0.5):
		
		if side not in [0,1]:
			raise Exception("Invalid side given to player!")

		if team_id not in [0,1]:
			raise Exception("Invalid team_id given to player!")

		self.id = Player.gen_id()
		# Coordiantes
		self.pos = Position(TODO)
		self.time = Time()
		self.skill = {"ability": 0.5} # Ability of the player (defined as float in [0, 1])
		
		# TODO build a dicionary
		self.battery = Battery.SimpleBattery()
		self.battery.set_ability(self.skill["ability"])

	def step(self, new_pos, rnd_number):
		#new_pos, success → movement, loss of energy
		# Update time
		# move the player
		# Update affinity
		current_aff = self.battery.get_affinity()

		# Return success state

	def start(self):
		"""
		Called at the start of the rally.
		"""
		self.battery.restart()


class Side:

	left = 1
	right = 0

class Court:

	#----Actions
	# → Setup
	def __init__(self, size, ability_t0=[0.5, 0.5], ability_t1=[0.5, 0.5]):
		
		assert len(size) == 2

		self.team0 = [ Player(team_id=0, side=Side.left,  ability=ability_t0[0]),
					   Player(team_id=0, side=Side.right, ability=ability_t0[1])]

		self.team1 = [ Player(team_id=1, side=Side.left,  ability=ability_t1[0]),
					   Player(team_id=1, side=Side.right, ability=ability_t1[1]) ]

		self.teams = [self.team0, self.team1]
		self.score = [0, 0] # Score of both the teams
		self.server = None
		self.receiver = None
		self.hitter = None

		# side 1 -> L side-r
		# side 0 -> R side-l

		self.shuttle = Shuttle()
		self.mesh = np.array.(size[0], size[1])

	def new_rally():
		# → It assigns service
	
		# → It generates new coordinates
		
		# → It calculates "norm" for the two players. min() → assigns player
		# → 
		# → Player.step(new_pos, rnd_) ==> Player return success status back to court
		# → Either the court continues the ralley
		# → Or assigns points and prepes new ralley
	
	def init_players(self):

		# Determine who serves
		team_id, serving_side = self.rule_determine_serve()
		player_idx = self.teams[team_id][1].side == serving_side		
		server = self.teams[team_id][player_idx]

		# Place players Within their quadrants
		#RODO get_rnd-quad(team_id, side)


		# Init Shuttle
		self.shuttle.set_team(team_id)
		self.shuttle.set_pos(*server.pos)


	def rule_determine_serve(self):
		"""
		Determines who takes the service.

		Returns serving position & switches player side if required.
		"""
		olds = self.oldscore

		# Determine serving team
		diff = [(n-o) for n, o in self.scores, self.oldscores]
		serving_team = diff.index(1)

		# If there is continuation → switch side
		if self.last_serve_team == serving_team:
			for players in self.teams[serving_team]:
				plater.switch_side()

		side_id = self.score[self.serving_team] % 2 != 0
		#Even -> True -> 1 -> L
		#Odd -> False -> 0 -> R

		serving_pos = (serving_team, side_id)
		return serving_pos

# 1-8
#_ _ _ _
 #1 4 2 8
 #1 5 8 3 -> b w r w -> next_set(1,2,4,8)
 #  _ _
 #  2 
 #  4
 #  8
 #  7
 #  _ _
 #1 2 4 8 -> b r r b -> nextt_set(2, 4)

 # black -> correct and same pos
 # red  -> correct but not same pos
 # white -> inncorrect


#8, 4
#w_t(no_r, no_w)
#b_t()
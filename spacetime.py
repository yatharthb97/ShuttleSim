
class Time:

	def __init__(self, rally, shot):
		"""
		Init takes a rally and shot time. Ideally integers.
		"""
		self.t_rally = rally
		self.t_shot = shot

	def __repr__(self):
		return f"[[{self.t_rally}-{self.shot}]]"




class Position:

	team_ss = (0, 1) # Team coordinate state space


	def __init__(self, team_id, x_len, y_len):
		"""
		Position has three components → [team_id, x_local, y_local]
		"""
		self.team = team_id

		self.x_ss = np.arange(x_len)
		self.y_ss = np.arange(y_len)

		self.xy = np.array([self.x_ss[0], self.y_ss[0]]) # x & y coordinates

	def set_pos(self, x, y):
		self.xy[0] = x
		self.xy[1] = y

	def get_pos(self):
		return [self.team, *self.xy]

	def get_xy(self):
		return self.xy


	def RandPositions(self, n=2):
		"""
		Returns a list of xy positions for players. It is not a 
		n : Number of players.

		TODO: Sample method has bias towards parallel 
		alignemnt of players -> [1,4] and [1,6] will not be generated.
		This is not an issue with high-resolution meshes.

		Solution:

		"""
		x_list = np.random.sample(self.x_ss, n)
		y_list = np.random.sample(self.y_ss, n)
		zipped = [list(pos) for pos in zip(x_list, y_list)]
		return zipped


	def RandLeftPosition(self):
		pass

	def RandRightPosition(self):
		pass


	def is_valid(self):
		return (self.team in self.team_ss) and (self.xy[0] in self.x_ss) and (self.xy[1] in self.y_ss)


	def disp(self):
		"""
		Calculates the inter-team or (inter-court) displacement.
		"""
		pass

	def is_same_side(self, other_pos):
		return self.team == other_pos.team

	def __repr__():
		return f"[[{self.team} - {self.xy} ]]"


class ShuttlePosition(Position):

	def __init__(self, team_id, x_len, y_len):
		super().__init__(team_id, x_len, y_len)

	def set_team(self, new_team):
		team = new_team

	def intra_disp(self):
		"""
		Calculates the intra-court displacement - which occurs across the net.
		"""
		if not self.is_same_team():
			pass
		else:
			return self.disp(other_pos)

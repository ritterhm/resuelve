# ===============================================================================
# Service path entry point mapping.
#
# Author: Miguel Ángel de la Rosa García
#
# This file is part of Evaluacion Backend project.
# ===============================================================================


# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------

# Core libraries
import dataclasses
import enum
import json

# Project libraries
import common


# -----------------------------------------------------------------------------
# Enumerations
# -----------------------------------------------------------------------------

class Level(enum.Enum):
	"""Goals by player level quotas enumeration."""

	A = 5
	B = 10
	C = 15
	Cuauh = 20

# -----------------------------------------------------------------------------
# Class Player
# -----------------------------------------------------------------------------

@dataclasses.dataclass
class Player:
	"""
		Player object. It must match JSON data request structure to automate
		serializing and deserializing.

		Attributes:
			Must match evaluacion backend description.
	"""

	nombre: str
	nivel: str
	goles: int
	sueldo: int
	bono: int
	sueldo_completo: float
	equipo: str


# -----------------------------------------------------------------------------
# Class Team
# -----------------------------------------------------------------------------

class Team:
	"""
		Class to hold and calculate all players data for each team.

		Attributes:
			list _players:
				Private holder for team members.
			int goals:
				Total team goals.
			int quota:
				Total goals quota for the team.
	"""

	def __init__(self) -> None:
		"""Class constructor. initializes class atributes"""

		self._players = []
		self.goals = 0
		self.quota = 0

	def calculate(self) -> None:
		"""Calculates wages for each team member."""

		team_bonus = self.goals / self.quota

		for player in self._players:
			player_bonus = (team_bonus + player.goles / Level[player.nivel].value) / 2
			player.sueldo_completo = round(player.sueldo + player.bono * player_bonus, 2)

	def player_add(self, player:Player) -> None:
		"""
			Add new player for team

			Arguments:
				Player player:
					Player object.
		"""

		self._players.append(player)
		self.goals += player.goles
		self.quota += Level[player.nivel].value


# -----------------------------------------------------------------------------
# Content generator rules
# -----------------------------------------------------------------------------

def calculate(environ:dict, service:object) -> None:
	"""
		Function to calculate players wages.

		Arguments:
			dict environ:
				System and project environment variables.
			service service:
				Caller service for entry point.
		Returns:
			None.
	"""

	# Team objects holder.
	teams = {}

	# Get content lenght.
	try:
		if 'CONTENT_LENGTH' in environ:
			data_size = int(environ.get('CONTENT_LENGTH', 0))
		else:
			data_size = 0
	except (ValueError):
		data_size = 0

	try:
	# Read json data
		data = environ['wsgi.input'].read(data_size)
		data = json.loads(data)
	except:
	# If data can't be read then return error as response.
		service.status = common.HTTPS.HTTPS_400
		service.response.append(repr(common.HTTPS.HTTPS_400.value))
		return


	#try:
	for chunk in data['jugadores']:
	# Test automated deserialize
		player = Player(**chunk)

		# Separate players by team
		if player.equipo not in teams:
			try:
				teams[player.equipo] = Team()
			except:
			# If player object can't be created the JSON is bad formed.
				service.status = common.HTTPS.HTTPS_400
				service.response.append(repr(common.HTTPS.HTTPS_400.value))
				return


		teams[player.equipo].player_add(player)

	# Calculate wages
	for key, team in teams.items():
		team.calculate()

	# Serialize output
	output = []

	for key, team in teams.items():
		for player in team._players:
			output.append(player.__dict__)

	service.response.append('{"jugadores": ')
	service.response.append(json.dumps(output))
	service.response.append('}')
	#except:
		## Server error
		#service.status = common.HTTPS.HTTPS_500
		#service.response.append(repr(common.HTTPS.HTTPS_500.value))

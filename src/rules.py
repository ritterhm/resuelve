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
import json

# Project libraries
import common


# -----------------------------------------------------------------------------
# class Player
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
	# If data can't be read then return error as response
		service.status = common.HTTPS.HTTPS_400
		service.response.append(repr(common.HTTPS.HTTPS_400.value))
		return


	for chunk in data['jugadores']:
	# Test automated deserialize
		player = Player(**chunk)
		print(player)

	# Return a copy of request data
	service.response.append(str(data))

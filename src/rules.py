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
import json

# Project libraries
import common


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

	# Return a copy of request data
	service.response.append(str(data))

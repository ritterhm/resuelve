# ===============================================================================
# Common project wide constants, enumerations and small objects header file.
#
# Author: Miguel Ángel de la Rosa García
#
# This file is part of Evaluacion Backend project.
# ===============================================================================


# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------

# Core libraries
import enum
import wsgiref.simple_server


# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# Encoding for string data
ENCODING = 'utf-8'


# -----------------------------------------------------------------------------
# Enumerations
# -----------------------------------------------------------------------------

class HTTPS(enum.Enum):
	"""
		HTTP status codes enumeraton for the service.
	"""

	HTTPS_200 = '200 Ok'
	HTTPS_400 = '400 Bad Request'
	HTTPS_404 = '404 Not Found'
	HTTPS_405 = '405 Method Not Allowed'
	HTTPS_500 = '500 Internal Server Error'

# ===============================================================================
# Service entrypoint file. Manages http requests and responses.
#
# Author: Miguel Ángel de la Rosa García
#
# This file is part of Evaluacion Backend project.
# ===============================================================================


# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------

# Type hints
from typing import Callable

# Project libraries
import common
import path


# -----------------------------------------------------------------------------
# Class Application
# -----------------------------------------------------------------------------

class Application:
	"""
		Manages HTTP calls.

		Attributes:
			headers:
				list Mandatory HTTP headers.
			str status:
				HTTP status code.
	"""

	def __init__(self) -> None:
		"""
			Application constructor. Sets default attributes for the object.

			Arguments:
				None.

			Returns:
				None.
		"""

		self.headers = [('Content-type', 'application/json; charset=utf-8')]
		self.status = None
		self.response = None

	def __call__(self, environ:dict, start_response:Callable) -> list:
		"""
			WSGI entry point.

			Arguments:
				dict environ:
					System environment variables.
				start_response:
					Callback response function

			Returns:
				list. Returns a list bytes list with response of the service.
		"""

		# Cleaning status and response
		self.status = common.HTTPS.HTTPS_200
		self.response = []

		path.runner(environ, self)

		# Response init.
		start_response(self.status.value, self.headers)

		return [chunk.encode(common.ENCODING) for chunk in self.response]

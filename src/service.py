#!/usr/bin/env python3

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


# -----------------------------------------------------------------------------
# Class Application
# -----------------------------------------------------------------------------

class Application:
	"""
		Manages HTTP calls.

		Attributes:
			headers:
				Mandatory HTTP headers.
			status:
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

		self.headers = [('Content-type', 'text/plain; charset=utf-8')]
		self.status = None

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

		# Response init.
		self.status = '200 OK'
		start_response(self.status, self.headers)

		# Response generation
		response = [("{}: {!s}\n".format(key, value)).encode("utf-8") for key, value in environ.items()]

		return response

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
#
# Type hints
from typing import Callable

# Project libraries
import common
import rules


# -----------------------------------------------------------------------------
# Path object
# -----------------------------------------------------------------------------

@dataclasses.dataclass
class Path:
	"""
		Path info type.

		Attributes:
			str method:
				HTTP method
			rule:
				Content generation function.
	"""

	method: str
	rule: Callable


# -----------------------------------------------------------------------------
# Global variables
# -----------------------------------------------------------------------------

# Valid path info dictionary
paths = {
	'/': Path('POST', rules.calculate)
}


# -----------------------------------------------------------------------------
# Path entrypoint runner
# -----------------------------------------------------------------------------

def runner(environ:dict, service:object) -> None:
	"""
		Path validation and running function. if API is right called pass the control to
		the rule content generation function.

		Arguments:
			dict environ:
				System and project environment variables.
			service service:
				Caller service for entry point.
		Returns:
			None.
	"""

	# APi call method and path info
	call_method = environ['REQUEST_METHOD']
	call_path = environ['PATH_INFO']

	for path, info in paths.items():
	#Check for each path in the sytem one that matches

		if path == call_path:
		# Path found! :)

			if call_method == info.method:
			# Check if path and method match, generate content.

				info.rule(environ, service)
			else:
			# Wrong method call, this validation only works for a path if
			# multiple methods is needed for same path refactoring it should be
			# refactored.

				service.status = common.HTTPS.HTTPS_405
				service.response.append('"' + common.HTTPS.HTTPS_405.value + '"')

			break;
	else:
	# Path not found.

		service.status = common.HTTPS.HTTPS_404
		service.response.append('"' + common.HTTPS.HTTPS_404.value + '"')

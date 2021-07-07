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
	'/': Path('POST', lambda e, s: s.response.append('Nice!'))
}


# -----------------------------------------------------------------------------
# Path validator
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

	call_method = environ['REQUEST_METHOD']
	call_path = environ['PATH_INFO']

	for path, info in paths.items():
		if path == call_path:
			if call_method == info.method:
				info.rule(environ, service)
			else:
				service.status = common.HTTPS.HTTPS_405
				service.response.append(common.HTTPS.HTTPS_405.value)

			break;
	else:
		service.status = common.HTTPS.HTTPS_404
		service.response.append(common.HTTPS.HTTPS_404.value)

#!/usr/bin/env python3

# ===============================================================================
# Service executable file. Wrapper for shell or gunicorn execution.
#
# Author: Miguel Ángel de la Rosa García
#
# This file is part of Evaluacion Backend project.
# ===============================================================================

"""
Handles JSON calls for Evaluacion de Backend

Usage:
	service.py [-h]
"""

# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------

# Core libraries
import sys
import wsgiref.simple_server

# Project libraries
import common
import service


# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# HTTP port for service binding.
PORT = 8080


# -----------------------------------------------------------------------------
# Initializations
# -----------------------------------------------------------------------------

# Clean docstring
__doc__ = __doc__.strip()


# -----------------------------------------------------------------------------
# Main code
# -----------------------------------------------------------------------------

# Application service instance
application = service.Application()

if __name__ == '__main__':

	if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
		print(__doc__)
		sys.exit(0)

	with wsgiref.simple_server.make_server('', PORT, application) as httpd:
		print('Serving evaluacion backend on port {}...'.format(PORT))
		httpd.serve_forever()

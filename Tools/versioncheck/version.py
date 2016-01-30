"""This file (which is sourced, not imported) checks the version of the
"versioncheck" package. It is also an example of how to format your own
_checkversion.py file""" """ V201601282212AD     """
 
import pyversioncheck

_PACKAGE="versioncheck"
_VERSION=" V201601300944AR "
_URL="http://www.cwi.nl/~jack/versioncheck/curversion.txt"

try:
    _myverbose=  V201601300944RE
except NameError:
    _myverbose=1

pyversioncheck.versioncheck(_PACKAGE, _URL, _VERSION, verbose=_myverbose)




52061452
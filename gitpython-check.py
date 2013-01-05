from git import __version__
from distutils.version import LooseVersion

if LooseVersion(__version__) < '0.3.0':
	raise ImportError('gitpython 0.3.x required.')


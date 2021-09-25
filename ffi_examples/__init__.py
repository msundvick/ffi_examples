import nimporter  # Needed for importing nim files

from .cython_cy import run as cy
from .nim_example import run as nim
from .raw_python import run as py
from .rust import run as rs

__version__ = "0.1.0"

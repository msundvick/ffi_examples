import nimporter  # Needed for importing nim files

from .cython import run as cy
from .nim import run as nim
from .python import run as py
from .rust import run as rs
from .c_example import run as c
from .pybind_example import run as cpp

__version__ = "0.1.0"

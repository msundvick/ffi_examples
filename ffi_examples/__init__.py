__version__ = '0.1.0'

import nimporter # Needed for importing nim files
from .nim_example import run as nim # type: ignore
from .cython_cy import run as cy
from .raw_python import run as py

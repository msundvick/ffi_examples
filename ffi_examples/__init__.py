import nimporter  # Needed for importing nim files

from .cython import run as cy
from .nim_example import run as nim
from .python import run as py
from .rust import run as rs
from .c_example import run as c
from .pybind_example import run as cpp


from juliacall import Main
Main.seval("using FfiExamples")
jl = Main.FfiExamples.run

__version__ = "0.1.0"

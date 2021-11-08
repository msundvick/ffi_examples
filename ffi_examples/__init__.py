from .python import run as py

from juliacall import Main

Main.seval("using FfiExamples")
jl = Main.FfiExamples.run

__version__ = "0.1.0"

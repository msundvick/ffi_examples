import json
import logging
import os
import shutil
from pathlib import Path
from typing import List, Union

import nimporter
import numpy
from Cython.Build import cythonize
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import Extension
from setuptools_rust import Binding, RustExtension

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))


def build(setup_kwargs):

    with open("ffi_examples/juliacalldeps.json", "r") as f:
        jl = json.load(f)

    jl["packages"]["FfiExamples"]["path"] = os.getcwd() + "/ffi_examples/FfiExamples"
    with open("ffi_examples/juliacalldeps.json", "w") as f:
        json.dump(jl, f)

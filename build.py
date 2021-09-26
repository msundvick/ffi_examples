import logging
import os
from typing import List, Union
import json

import nimporter
import numpy
from Cython.Build import cythonize
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import Extension
from setuptools_rust import Binding, RustExtension

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))


def build(setup_kwargs):
    logging.info("Before: %s", setup_kwargs)
    name = setup_kwargs["packages"][0]

    extensions: List[Union[Extension, Pybind11Extension]] = [
        Extension(
            f"{name}.c_example",
            [f"{name}/c/example.c"],
            language="c",
            py_limited_api=True,
            define_macros=[("Py_LIMITED_API", None)],
        ),
        Pybind11Extension(
            f"{name}.pybind_example",
            [f"{name}/cpp/cpp_example.cpp"],
        )
    ]

    # Build
    setup_kwargs.update(
        {
            "ext_modules": cythonize(
                f"{name}/**/*_cy.py",
                language_level=3,
                annotate=True,
                compiler_directives={"linetrace": True},
            )
            + extensions
            + nimporter.build_nim_extensions(),
            "rust_extensions": [
                RustExtension(
                    f"{name}/rust",
                    path="Cargo.toml",
                    binding=Binding.PyO3,
                    debug=False,
                )
            ],
            "install_requires": ["numpy", "setuptools_rust"],
            "include_dirs": [numpy.get_include()],
            "zip_safe": False,
        }
    )

    logging.info("After: %s", setup_kwargs)


    with open("juliacalldeps.json", "r") as f:
        jl = json.load(f)

    jl["packages"]["FfiExamples"]["path"] = os.getcwd()
    with open("juliacalldeps.json", "w") as f:
        json.dump(jl, f)

    import juliacall
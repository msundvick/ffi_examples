import logging
import os
from typing import List

import nimporter
import numpy
from Cython.Build import cythonize
from setuptools import Extension
from setuptools_rust import Binding, RustExtension

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))


def build(setup_kwargs):
    logging.info("Before: %s", setup_kwargs)
    name = setup_kwargs['packages'][0]

    cython_extensions: List[str] = [f"{name}/cython_cy.pyx"]
    extensions: List[Extension] = [
        # f"{name}/c_example.c",
        # f"{name}/cpp_example.cpp",
    ]

    # Build
    setup_kwargs.update(
        {
            "ext_modules": cythonize(
                cython_extensions,
                language_level=3,
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

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ffi_examples',
 'ffi_examples.cython',
 'ffi_examples.nim',
 'ffi_examples.python']

package_data = \
{'': ['*'], 'ffi_examples': ['c/*', 'cpp/*']}

install_requires = \
['juliacall @ git+https://github.com/cjdoris/PythonCall.jl@master',
 'numpy>=1.21.2,<2.0.0']

setup_kwargs = {
    'name': 'ffi-examples',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Michael Sundvick',
    'author_email': 'michsund@outlook.co.nz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)

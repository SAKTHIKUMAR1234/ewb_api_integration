# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import find_packages, setup

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# Read the version without importing the app during an isolated package build.
about = {}
exec((Path(__file__).parent / "ewb_api_integration" / "__init__.py").read_text(), about)
version = about["__version__"]

setup(
	name='ewb_api_integration',
	version=version,
	description='Implementation of Eway Bill API Integration for India',
	author='Aerele',
	author_email='admin@aerele.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

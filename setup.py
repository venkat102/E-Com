from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecom/__init__.py
from ecom import __version__ as version

setup(
	name="ecom",
	version=version,
	description="Ecom",
	author="Venkat",
	author_email="Venkat",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

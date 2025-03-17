from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in enshaa/__init__.py
from enshaa import __version__ as version

setup(
	name="enshaa",
	version=version,
	description="Trial Balance customization app",
	author="Greycube Technologies",
	author_email="admin@greycube.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

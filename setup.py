from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vdemo_app/__init__.py
from vdemo_app import __version__ as version

setup(
	name="vdemo_app",
	version=version,
	description="it is a demo app",
	author="vikas ",
	author_email="mailtovikas@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecs_icd/__init__.py
from ecs_icd import __version__ as version

setup(
	name="ecs_icd",
	version=version,
	description="ecs_icd",
	author="ecs_icd",
	author_email="ecs_icd",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

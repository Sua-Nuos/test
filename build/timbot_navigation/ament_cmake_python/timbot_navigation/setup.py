from setuptools import find_packages
from setuptools import setup

setup(
    name='timbot_navigation',
    version='0.0.0',
    packages=find_packages(
        include=('timbot_navigation', 'timbot_navigation.*')),
)

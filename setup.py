from setuptools import setup

with open('requirements.txt') as file:
    requirements = [x.strip() for x in file.readlines()]

setup(
    name='aoc_package',
    version='0.0.1',
    description='package template for AOC',
    install_requires=requirements
)
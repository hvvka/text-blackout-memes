from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

setup(
    name='text-blackout-memes',
    version='0.0.1',
    license='MIT',
    description='Automated text blackout memes creation',
    long_description=open('README.md').read(),
    url='https://github.com/hvvka/text-blackout-memes',
    author='Puppies',
    author_email='hania.grodzicka@gmail.com',
    packages=find_packages()
)

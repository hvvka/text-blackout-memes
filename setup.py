from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

setup(
    name='cross-out-memes',
    version='0.0.1',
    license='MIT',
    description='Automated cross-out letters memes creation',
    long_description=open('README.md').read(),
    url='https://github.com/hvvka/cross-out-memes',
    author='Puppies',
    author_email='hania.grodzicka@gmail.com',
    packages=find_packages()
)

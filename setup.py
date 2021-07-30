from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='apt-ios-repo',
    version='0.1',
    packages=['apt_ios_repo'],
    url='https://github.com/arturgoms/python-apt-ios-repo',
    license='MIT',
    author='Artur Gomes',
    author_email='contato@arturgomes.com.br',
    description='Python library to manage and query APT repositories from iOS Jailbreak community',
    long_description_content_type='text/markdown',
    long_description=long_description,
    python_requires='>=3.5'
)
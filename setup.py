#-------------------------------------------------------------------------------
# pss: setup.py
#
# Setup/installation script.
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------------
import os, sys
try:
    from setuptools import setup
    use_setuptools = True
except ImportError:
    from distutils.core import setup
    use_setuptools = False

if use_setuptools:
    extra_args = {
        'entry_points': {
            'console_scripts': 'pss = psslib.pss:main'
        },
    }
else:
    extra_args = {
        'scripts': ['scripts/pss.py', 'scripts/pss'],
    }


try:
    with open('README.rst', 'rt') as readme:
        description = '\n' + readme.read()
except IOError:
    # maybe running setup.py from some other dir
    description = ''


setup(
    # metadata
    name='pss',
    description='Tool for grepping through source code',
    long_description=description,
    license='Public domain',
    version='1.39',
    author='Eli Bendersky',
    maintainer='Eli Bendersky',
    author_email='eliben@gmail.com',
    url='https://github.com/eliben/pss',
    platforms='Cross Platform',
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',],

    packages=['psslib', 'psslib.colorama'],

    **extra_args
)


#!/usr/bin/env python

from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md').read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.3.1'

setup(
    name='haxor',
    version=version,
    install_requires=requirements,
    author='Avinash Sajjanshetty',
    author_email='a@sajjanshetty.com',
    packages=find_packages(),
    include_package_data=True,
    test_suite='tests',
    url='https://github.com/avinassh/haxor/',
    license='MIT',
    description='Unofficial Python wrapper for Hacker News API',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)

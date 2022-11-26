#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
        'Click>=7.0', 
        'pydantic==1.10.2',
        'uplink==0.9.7',
        ]

test_requirements = [ ]

setup(
    author="Barak Avrahami",
    author_email='baraka@coregen.io',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An API client for go-shiori web server",
    entry_points={
        'console_scripts': [
            'shiori=shiori.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='shiori',
    name='shiori',
    packages=find_packages(include=['shiori', 'shiori.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/andecy64/shiori',
    version='0.0.0',
    zip_safe=False,
)
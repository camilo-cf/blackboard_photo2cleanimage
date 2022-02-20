#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

file_requirements = open('requirements.txt', 'r')
requirements = file_requirements.readlines()
requirements = [line.replace("\n", "") for line in requirements] 

setup(
    author="Camilo Caceres F",    
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="Image API converter from blackboard to B/W.",
    install_requires=requirements,
    license="GNU General Public License v3",
    include_package_data=True,
    keywords='blackboard_photo2cleanimage',
    name='blackboard_photo2cleanimage',
    packages=find_packages(include=['blackboard_photo2cleanimage', 'blackboard_photo2cleanimage.*']),
    test_suite='tests',
    url='https://github.com/camilo-cf/blackboard_photo2cleanimage',
    version='0.1.0',
    zip_safe=False,
)
#!/usr/bin/env python
from setuptools import setup

setup(
    name="django-cronitor-tools",
    author="Dan Paulson",
    author_email="danpaulson@gmail.com",
    description="Tools for cronitor in  Django",
    version='1.0.0',
    install_requires=[
        'django',
        'cronitor',
        'requests',
    ]
)

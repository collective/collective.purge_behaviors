# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='collective.purge_behaviors',
    version='0.2',
    description='A set of dexterity behaviors for Plone that are assignable to custom dexterity types for complex system setups',
    long_description=read('README.rst') +
                     read('HISTORY.rst') +
                     read('LICENSE'),
    classifiers=[
        "Programming Language :: Python",
    ],
    author='eleddy',
    author_email='elizabeth.leddy@gmail.com',
    url='https://github.com/collective/collective.purge_behaviors',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['collective'],
    install_requires=[
        'setuptools',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.api',
            'nose',
            'nose-selecttests',
            'coverage',
            'unittest2',
            'flake8',
        ],
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
    """,
    include_package_data=True,
    zip_safe=False,

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.zcml', 'LICENSE'],
    },
)

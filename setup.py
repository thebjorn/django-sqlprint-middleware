#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""django-sqlprint-middleware
"""
import io

from setuptools import setup

version = '0.1.0'


setup(
    name='django-sqlprint-middleware',
    version=version,
    packages=['django_sqlprint_middleware'],
    install_requires=[
        'pygments-pprint-sql',
        'Django'
    ],
    long_description=io.open('README.rst', encoding='utf8').read(),
    url='https://github.com/thebjorn/django-sqlprint-middleware',
    license='MIT',
    author='bjorn',
    author_email='bp@datakortet.no',
    description='Display module dependencies',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

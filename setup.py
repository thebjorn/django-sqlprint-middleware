#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""django-sqlprint-middleware - pretty-print Django's SQL statments.
"""
import io

from setuptools import setup

version = '0.1.4'


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
    description="Pretty print Django's SQL statments",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
    ]
)

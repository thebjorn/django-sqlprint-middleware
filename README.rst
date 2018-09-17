.. coding: utf-8

==========================
django-sqlprint-middleware
==========================

Middleware that pretty prints Django's sql statements.

Installation
------------
Install from PyPI::

    pip install django-sqlprint-middleware

then add it to the `MIDDLEWARE` settings in your `settings.py` file::

    MIDDLEWARE = (
        ...
        'django_sqlprint_middleware.SqlPrintMiddleware',
        ...
    )

(Use `MIDDLEWARE_CLASSES` in older Djangos.)

This middleware is not order sensitive so you can put it at any position in
the list of classes.


Settings
--------
The following settings control the behavior (all of these have defaults).

DEBUG or TESTING
    Either of these need to be True for the middleware to run.

SQLPRINT_MIDDLEWARE
    Set to False to skip middleware without removing it.

X_DB_HITS
    Set to false to prevent db hits being sent in the response header 'X-DB-hits'

SQLPRINT_MAX_QUERIES
    Raise an exception if the number of queries for a view is greater than this.
    Default is 1200 (zero means no check).

SQLPRINT_MIN_QUERIES
    For less output you can set this to the number of queries a view can make before
    queries are printed (default is zero).

# -*- coding: utf-8 -*-
"""
Base version of package/tasks.py, created by

    package/root/dir> dk-tasklib install

(it should reside in the root directory of your package)

This file defines tasks for the Invoke tool: http://www.pyinvoke.org

Basic usage::

    inv -l               # list all available tasks
    inv build -f         # build everything, forcefully
    inv build --docs     # only build the docs

dk-tasklib is a library of basic tasks that tries to automate common tasks.
dk-tasklib will attempt to install any tools/libraries/etc. that are required,
e.g. when running the task to compile x.less to x.css, it will check that
the lessc compiler is installed (and if not it will attempt to install it).

This file is an initial skeleton, you are supposed to edit and add to it so it
will fit your use case.


"""
# pragma: nocover
from __future__ import print_function
import os

from dkfileutils.path import Path
from invoke import Collection

from dktasklib import docs as doctools
from dktasklib import version, upversion
from dktasklib.package import Package, package
from dktasklib.publish import publish

#: where tasks.py is located (root of package)
DIRNAME = Path(os.path.dirname(__file__))


# individual tasks that can be run from this project
ns = Collection(
    doctools,
    version, upversion,
    publish,
)
ns.configure({
    'pkg': Package(),
    'run': {
        'echo': True
    }
})

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#       Copyright (C) 2005-2007 Carabos Coop. V. All rights reserved
#       Copyright (C) 2008-2013 Vicent Mas. All rights reserved
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#       Author:  Vicent Mas - vmas@vitables.org

"""
Site configuration module.

This module indicates the full install path of the ``ViTables`` package to the
running :meth:`vitables.vtapp.VTApp` instance.

Mac OS X boxes use the module as is.

Misc variables:

* __docformat__
* INSTALLDIR
* ICONDIR
* DOCDIR
* PLUGINSDIR
"""

__docformat__ = 'restructuredtext'

import sys
import os.path

PACKAGEDIR = os.path.dirname(__file__)
FROZEN = getattr(sys, 'frozen', False)
if FROZEN:
    DATADIR = os.path.join(os.path.dirname(sys.executable), 'vitables')
else:
    DATADIR = PACKAGEDIR
ICONDIR = os.path.join(DATADIR, "icons")
DOCDIR = os.path.join(DATADIR, "htmldocs")
PLUGINSDIR = os.path.join(DATADIR, "plugins")
PLUGINSCODEDIR = os.path.join(PACKAGEDIR, "plugins")


def resource_path(module_path, fname):
    """
    returns an absolute path for the *fname* file, relative to the module at
    *module_path*.
    eg. resource_path(__file__, "about.ui")
    """
    rel_path = os.path.relpath(os.path.dirname(module_path), PACKAGEDIR)
    return os.path.join(DATADIR, rel_path, fname)
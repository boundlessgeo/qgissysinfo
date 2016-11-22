# -*- coding: utf-8 -*-

"""
***************************************************************************
    system_info.py
    ---------------------
    Date                 : November 2016
    Copyright            : (C) 2016 Boundless, http://boundlessgeo.com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alexander Bruy'
__date__ = 'November 2016'
__copyright__ = '(C) 2016 Boundless, http://boundlessgeo.com'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import platform

from PyQt4.Qt import PYQT_VERSION_STR
from PyQt4.QtCore import QT_VERSION_STR
from sip import SIP_VERSION_STR

from PyQt4.QtGui import QApplication, QImageReader
from PyQt4.QtSql import QSqlDatabase


def systemInfo():
    pass


def pythonInfo():
    info = ["Python information",
            "------------------",
            "Python implementation: {implementation}"
            "Python version: {version} {build}",
           ]
    info = os.linesep.join(info)
    info = info.format(implementation = platform.python_implementation(),
                       version = platform.python_version(),
                       build = platform.python_build()
                      )
    return info


def qtInfo():
    info = ["Qt/PyQt information",
            "-------------------",
            "Qt version: {qtVersion}",
            "PyQt version: {pyqtVersion}",
            "SIP version: {sipVersion}",
            "Qt library paths:",
            "{qtLibs}",
            "Qt database plugins:",
            "{qtDbPlugins}",
            "Qt image plugins:",
            "{qtImagePlugins}"
           ]

    libPaths = os.linesep.join(
            ["\t{}".format(i) for i in QApplication.libraryPaths()])
    dbPlugins = os.linesep.join(
            ["\t{}".format(i) for i in QSqlDatabase.drivers()])
    imagePlugins = os.linesep.join(
            ["\t{}".format(i) for i in QImageReader.supportedImageFormats()])

    info = os.linesep.join(info)
    info = info.format(qtVersion = QT_VERSION_STR,
                       pyqtVersion = PYQT_VERSION_STR,
                       sipVersion = SIP_VERSION_STR,
                       qtLibs = libPaths,
                       qtDbPlugins = dbPlugins,
                       qtImagePlugins = imagePlugins
                      )
    return info

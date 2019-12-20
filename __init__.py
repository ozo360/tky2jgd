# -*- coding: utf-8 -*-
"""
/***************************************************************************
 tky2jgd
                                 A QGIS plugin
 日本測地系に基づく経緯度を世界測地系に基づく経緯度へ変換する
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-06-29
        copyright            : (C) 2019 by ozaki
        email                : ozaki360@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load tky2jgd class from file tky2jgd.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tky2jgd import tky2jgd
    return tky2jgd(iface)
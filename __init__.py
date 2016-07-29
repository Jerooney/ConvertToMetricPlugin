# Copyright (c) 2015 Jaime van Kessel
# The BarbarianPlugin is released under the terms of the AGPLv3 or higher.

from . import BarbarianPlugin
from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("MetricScalePlugin")
def getMetaData():
    return {
        "type": "extension",
        "plugin":
        {
            "name": "Metric Scale plugin",
            "author": "Jaime van Kessel",
            "version": "2.2",
            "api": 3,
            "description": i18n_catalog.i18nc("Description of plugin","This extension quickly converts models drawn in inches to metric values.")
        }
    }

def register(app):
    return { "extension": MetricScalePlugin.MetricScalePlugin()}

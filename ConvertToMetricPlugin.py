from UM.Extension import Extension
from UM.Scene.Selection import Selection
from UM.Math.Vector import Vector

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("ConvertToMetricPlugin")

class ConvertToMetricPlugin(Extension):
    def __init__(self):
        super().__init__()
        self.addMenuItem(i18n_catalog.i18n("Convert selected model"), self.convertToMetric)

    def convertToMetric(self):
        selected_nodes = Selection.getAllSelectedObjects()
        for node in selected_nodes:
            node.scale(Vector(25.4,25.4,25.4))

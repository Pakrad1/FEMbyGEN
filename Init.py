import FreeCAD
from TranslateUtils import translate
import FreeCADGui
import os
LOCATION = os.path.join("Mod","FEMbyGEN","fembygen")

FreeCADGui.addLanguagePath(os.path.join(FreeCAD.getUserAppDataDir(),LOCATION,"translations"))
print(translate("FEMbyGEN","FEMbyGEN Workbench loaded"))

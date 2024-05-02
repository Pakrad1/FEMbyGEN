import FreeCAD
from TranslateUtils import translate
import FreeCADGui
FreeCADGui.addLanguagePath(os.path.join(FreeCAD.getUserAppDataDir(),"/Mod/FEMbyGEN/fembygen/translations"))
print(translate("FEMbyGEN","FEMbyGEN Workbench loaded"))

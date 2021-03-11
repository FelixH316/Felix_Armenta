# DESCRIPTION: Main de la GUI, desde aqui se debe ejecutar el proyecto
# AUTHOR: Félix Armenta Aguiñaga - IECA PADTS 3

from PySide2.QtWidgets import QApplication
from proControlGUI import Gui
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Gui()
    window.show()
    sys.exit(app.exec_())

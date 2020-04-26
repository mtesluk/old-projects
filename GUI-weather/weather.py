from files.window import Window
from PyQt4 import QtGui
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

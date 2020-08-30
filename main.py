from PyQt5 import QtWidgets, QtCore
import source.py_ui.screen as screen
import sys

import source.tools.Containers as Containers
import source.tools.Constants as Constants
 
 
class mywindow(QtWidgets.QMainWindow, screen.Ui_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for key in Constants.DATA.keys():
            t = Containers.Tab(None, Constants.DATA[key])
            self.tabWidget.addTab(t.out, key)

    def resizeEvent(self, event):
        # old_size = [event.oldSize().width(), event.oldSize().height()]
        current_size = [event.size().width(), event.size().height()]

        self.tabWidget.setGeometry(0, 0, current_size[0], current_size[1] - 50)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())

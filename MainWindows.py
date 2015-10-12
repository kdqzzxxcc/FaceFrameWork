__author__ = 'DELL'

import sys
from PyQt4 import QtGui, QtCore, Qt
from Camera import CameraWidget
from Display import Display

from PyQt4.QtCore import Qt

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self._action()
        self.init()

    def init(self):
        self.resize(1280, 960)
        self.setWindowTitle('FaceFrameWork')
        self.split = QtGui.QSplitter(Qt.Horizontal, self)
        self.left = CameraWidget(self.split)
        self.split.setStretchFactor(0, 1)
        self.right = Display(self.split)
        self.split.setStretchFactor(1, 3)
        self.setCentralWidget(self.split)

        menu = self.menuBar()
        file = menu.addMenu('File')
        file.addAction(self._open_file)
        file.addAction(self._close_file)

    def _action(self):
        self._open_file = QtGui.QAction('open', self)
        self._open_file.triggered.connect(self._open)

        self._close_file = QtGui.QAction('close', self)
        self._close_file.triggered.connect(self.close)

    def _open(self):
        file_name = unicode(QtGui.QFileDialog().getOpenFileName(self,'Open', self.tr(''), self.tr('*')))
        if len(file_name) == 0:
            return False
        ### TODO READ PIC IN CAMERAWIDGET




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
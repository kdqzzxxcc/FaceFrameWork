__author__ = 'KDQ'

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
        # self.resize(1280, 960)
        self.resize(500, 500)
        self.setWindowTitle('FaceFrameWork')

        # set split layout

        self.split = QtGui.QSplitter(Qt.Horizontal, self)

        # left widget is camera widget, this widget deal with take photos through OpenCV Lib
        # ans transfer OpenCV Pic to PyQt4 QImage, then use QPainter to show PyQt Pic

        self.left = CameraWidget(self.split)
        self.split.setStretchFactor(0, 1)

        # right widget is display widget, this widget deal with process face detection algorithm,
        # and show result in it

        self.right = Display(self.split)
        self.split.setStretchFactor(1, 2)

        self.setCentralWidget(self.split)

        # this is menu bar, in this instance, just use one to load pic

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
        self.right._open(file_name)
        ### TODO READ PIC IN DISPLAY WIDGET
        # Show pic in right widget and process face detection algorithm





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
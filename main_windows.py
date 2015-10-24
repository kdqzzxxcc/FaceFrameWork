__author__ = 'KDQ'

import sys
from PyQt4 import QtGui, QtCore, Qt
from main_camera import Combine
from display_result import Display
import os
from PyQt4.QtCore import Qt

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        if os.path.exists('./temp') == False:
            os.mkdir('./temp')
        # self._action()
        self.init()
        # self.right._open('./temp/default.jpg')

    def init(self):
        self.showMaximized()
        # self.resize(1280, 960)
        self.setWindowTitle('FaceFrameWork')

        # set split layout

        self.split = QtGui.QSplitter(Qt.Horizontal, self)

        # left widget is camera widget, this widget deal with take photos through OpenCV Lib
        # ans transfer OpenCV Pic to PyQt4 QImage, then use QPainter to show PyQt Pic

        self.left = Combine(self.split)

        # right widget is display widget, this widget deal with process face detection algorithm,
        # and show result in it

        self.right = Display(self.split)
        self.split.setStretchFactor(1, 1)
        self.setCentralWidget(self.split)

        # this is menu bar, in this instance, just use one to load pic
        self._action()
        menu = self.menuBar()
        file = menu.addMenu('File')
        action = menu.addMenu('Action')
        file.addAction(self._open_file)
        file.addAction(self._close_file)
        action.addAction(self._photo)
        action.addAction(self._start)
        action.addAction(self._pause)

    def _action(self):
        self._open_file = QtGui.QAction('Open', self)
        self._open_file.setShortcut('Ctrl+O')
        self._open_file.triggered.connect(self._open)

        self._close_file = QtGui.QAction('Close', self)
        self._close_file.triggered.connect(self.close)

        self._photo = QtGui.QAction('Photo', self)
        self._photo.setShortcut('Ctrl+Q')
        self._photo.triggered.connect(lambda :self.left.down._take_photo())

        self._start = QtGui.QAction('Start', self)
        self._start.setShortcut('Ctrl+S')
        self._start.triggered.connect(lambda :self.left.down._start())

        self._pause = QtGui.QAction('Pause', self)
        self._pause.setShortcut('Ctrl+P')
        self._pause.triggered.connect(lambda :self.left.down._pause())

    def _open(self):
        file_name = unicode(QtGui.QFileDialog().getOpenFileName(self,'Open', self.tr(''), self.tr('*')))
        if len(file_name) == 0:
            return False
        self.right._open(file_name)
        # Show pic in right widget and process face detection algorithm


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
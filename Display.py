# coding=utf-8
__author__ = 'KDQ'


from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


class Display(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Display, self).__init__(parent)
        self.initVBox()

    def initVBox(self):
        self.up = QtGui.QLabel(self)
        self.up.setAlignment(Qt.AlignCenter)

        self.down = QtGui.QLabel(self)
        self.down.setAlignment(Qt.AlignCenter)
        self.down.setText('TEST')

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.up)
        layout.addWidget(self.down)
        layout.addStretch(1)

        self._open('./temp/default.jpg')
        self.setLayout(layout)

    def initSpliter(self):
        # layout = QtGui.QVBoxLayout()
        self.split = QtGui.QSplitter(Qt.Vertical, self.parent())
        self.up = QtGui.QLabel(self.split)
        self.up.setAlignment(Qt.AlignCenter)

        self.down = QtGui.QLabel(self.split)
        self.down.setAlignment(Qt.AlignCenter)
        self.down.setText('test')
        self.split.setStretchFactor(0, 1)
        self.split.setStretchFactor(1, 1)
        self._open('./temp/default.jpg')
        layout = QtGui.QVBoxLayout(self.split)
        self.setLayout(layout)


    def _open(self, file_path):
        # print file_path
        pix = QtGui.QPixmap(file_path)
        # print self.parent().size()
        pix = pix.scaledToHeight(960 / 3)
        pix = pix.scaledToWidth(1280 / 3)
        self.up.setPixmap(pix)
        ### TODO PROCESS FACE DETECTION ALGORITHM



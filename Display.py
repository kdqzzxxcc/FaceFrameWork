# coding=utf-8
__author__ = 'KDQ'


from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


class Display(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Display, self).__init__(parent)

        # layout = QtGui.QVBoxLayout()
        self.split = QtGui.QSplitter(Qt.Vertical, parent)
        # self.uup = QtGui.QLabel(self.split)
        # self.uup.setText(QtCore.QString.fromUtf8('照片'))
        # self.split.setStretchFactor(9, 1)
        self.up = QtGui.QLabel(self.split)

        self.up.setAlignment(Qt.AlignCenter)
        self.down = QtGui.QLabel(self.split)
        self.down.setAlignment(Qt.AlignCenter)

        # self.split.setStretchFactor(0, 7)
        # self.split.setStretchFactor(1, 3)
        self.down.setText('test')
        self._open('./temp/default.jpg')
        layout = QtGui.QVBoxLayout(self.split)
        self.setLayout(layout)
        # self.split.setSizes([1,1])

        # self.split.setStretchFactor(9, 1)
        # self._layout = QtGui.QGridLayout(self)


        # self.show_pic = QtGui.QLabel(self)
        #
        # self.result_pic = QtGui.QLabel(self)
        #
        # self._layout.addWidget(self.show_pic, 0, 0)
        # self._layout
        # self.show_pic.setPixmap()

        # self._layout.addWidget(self.show_pic)


    def _open(self, file_path):
        print file_path
        pix = QtGui.QPixmap(file_path)
        print self.parent().size()
        pix = pix.scaledToHeight(960 / 3)
        pix = pix.scaledToWidth(1280 / 3)
        self.up.setPixmap(pix)
        ### TODO PROCESS FACE DETECTION ALGORITHM



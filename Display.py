__author__ = 'KDQ'


from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


class Display(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Display, self).__init__(parent)

        self.split = QtGui.QSplitter(Qt.Vertical, parent)

        self.split.setStretchFactor(9, 1)
        self.up = QtGui.QLabel(self.split)
        self.up.setAlignment(Qt.AlignCenter)
        self.down = QtGui.QLabel(self.split)
        self.down.setAlignment(Qt.AlignCenter)

        # self.split.setStretchFactor(9, 1)
        self.down.setText('test')

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
        pix = pix.scaledToHeight(200)
        self.up.setPixmap(pix)
        ### TODO PROCESS FACE DETECTION ALGORITHM



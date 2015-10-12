__author__ = 'KDQ'


from PyQt4 import QtGui, QtCore

class Display(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Display, self).__init__(parent)

        # self._layout = QtGui.QGridLayout(self)

        # self.show_pic = QtGui.QLabel(self)
        #
        # self.show_pic.setPixmap()

        # self._layout.addWidget(self.show_pic)


    def _open(self, file_path):
        print file_path
        self._layout = QtGui.QGridLayout(self)
        self.show_pic = QtGui.QLabel(self)
        pix = QtGui.QPixmap(file_path)
        pix = pix.scaledToHeight(200)
        self.show_pic.setPixmap(pix)

        self._layout.addWidget(self.show_pic, 0, 0)
        self.setLayout(self._layout)



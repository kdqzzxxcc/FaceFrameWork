# coding=utf-8
__author__ = 'KDQ'


from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from Algorithm import init, run_algorithm
display = {
    0:u"无表情",
    1:u"高兴",
    2:u"伤心",
    3:u"惊讶",
    4:u"生气",
    5:u"沮丧",
    6:u"害怕"
}
class Display(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Display, self).__init__(parent)
        self.initVBox()
        init()

    def initVBox(self):
        self.uup = QtGui.QLabel(QtCore.QString.fromUtf8('识别图像'))
        self.uup.setAlignment(Qt.AlignCenter)
        self.up = QtGui.QLabel(self)
        self.up.setAlignment(Qt.AlignCenter)

        self.down = QtGui.QLabel(self)
        self.down.setAlignment(Qt.AlignCenter)
        self.down.setText('TEST')
        self.down.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.uup)
        layout.addWidget(self.up)
        layout.addStretch(2)
        layout.addWidget(self.down)
        # layout.addStretch(1)

        self._open('./temp/default.jpg')
        self.setLayout(layout)

    def initSpliter(self):
        # layout = QtGui.QVBoxLayout()
        self.split = QtGui.QSplitter(Qt.Vertical, self.parent())
        self.up = QtGui.QLabel(self.split)
        self.up.setAlignment(Qt.AlignCenter)
        # self.up.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        # self.up.setStyleSheet('border:10px solid black;border-radius:5px')
        self.down = QtGui.QLabel(self.split)
        self.down.setAlignment(Qt.AlignCenter)
        self.down.setText('test')
        self.down.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        self.down.setLineWidth(10)

        # self.down.setStyleSheet('border:10px solid black;border-radius:5px')
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
        if file_path != './temp/default.jpg':
            result = run_algorithm(file_path)
            self.down.setText(QtCore.QString.fromUtf8(display[int(result[0])]))
        ### TODO PROCESS FACE DETECTION ALGORITHM


class test(QtGui.QWidget):

    def __init__(self, parent=None):
        super(test, self).__init__(parent)
        self.x = QtGui.QLabel('test')
        self.y = QtGui.QLabel('test1')
        layout = QtGui.QHBoxLayout()
        self.x.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        self.y.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        layout.addWidget(self.x)
        layout.addWidget(self.y)
        self.setLayout(layout)
        self.resize(500, 500)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    main = test()
    main.show()
    sys.exit(app.exec_())
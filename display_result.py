# coding=utf-8
__author__ = 'KDQ'


from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from main_algorithm import init, run_algorithm
right_image_height = 400
right_image_width = 500
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
        self.uup.setFixedHeight(25)
        self.up = QtGui.QLabel(self)
        self.up.setAlignment(Qt.AlignCenter)
        self.up.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        # self.up.setFixedHeight(400)
        self.up.setFixedSize(right_image_width, right_image_height)
        self.down = QtGui.QLabel(self)
        self.down.setAlignment(Qt.AlignCenter)
        self.down.setText(QtCore.QString.fromUtf8('请输入图片'))
        self.down.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        self.down.setFixedHeight(50)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.uup)
        # layout.addStretch(1)
        layout.addWidget(self.up)
        # layout.addStretch(1)
        layout.addWidget(self.down)
        layout.addStretch(1)
        self.setLayout(layout)
        self._open('./temp/default.jpg')


    def initSpliter(self):
        # layout = QtGui.QVBoxLayout()
        self.split = QtGui.QSplitter(Qt.Vertical, self.parent())
        self.up = QtGui.QLabel(self.split)
        self.up.setAlignment(Qt.AlignCenter)
        self.split.setStretchFactor(0, 1)
        # self.up.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        # self.up.setStyleSheet('border:10px solid black;border-radius:5px')
        self.down = QtGui.QLabel(self.split)
        self.down.setAlignment(Qt.AlignCenter)
        self.down.setText(QtCore.QString.fromUtf8('请输入图片'))
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
        pix = pix.scaled(right_image_width, right_image_height)
        # pix = pix.scaledToHeight(500 / 2)
        # pix = pix.scaledToWidth(1200 / 3)
        self.up.setPixmap(pix)
        if file_path != './temp/default.jpg':
            result = run_algorithm(file_path)
            if result is None:
                self.down.setText(QtCore.QString.fromUtf8("无法检测到人脸，请检查图片分辨率"))
            else:
                self.down.setText(QtCore.QString.fromUtf8(u"检测结果："+display[int(result[0])]))
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
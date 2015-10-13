__author__ = 'KDQ'

from PyQt4 import QtGui
from PyQt4 import QtCore
import cv2
import time

class OpenCVtoPyQt(QtGui.QImage):

    def __init__(self, opencvBgrImg):
        depth, nChannels = opencvBgrImg.depth, opencvBgrImg.nChannels
        if depth != cv2.cv.IPL_DEPTH_8U or nChannels != 3:
            raise ValueError("the input image must be 8-bit, 3-channel")
        w, h = cv2.cv.GetSize(opencvBgrImg)
        opencvRgbImg = cv2.cv.CreateImage((w, h), depth, nChannels)
        # it's assumed the image is in BGR format
        cv2.cv.CvtColor(opencvBgrImg, opencvRgbImg, cv2.cv.CV_BGR2RGB)
        self._imgData = opencvRgbImg.tostring()
        super(OpenCVtoPyQt, self).__init__(self._imgData, w, h, QtGui.QImage.Format_RGB888)


class CameraWidget(QtGui.QWidget):

    def __init__(self, parent=None, camera_index=0):
        super(CameraWidget, self).__init__(parent)
        self.frame = None
        self.fps = 30
        self._camera = cv2.cv.CaptureFromCAM(camera_index)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000/ self.fps)
        self.timer.timeout.connect(self._get_frame)
        self.pause = False
        self.timer.start()

    def _start(self):
        self.timer.start()

    def _stop(self):
        self.timer.stop()

    def _pause(self):
        if self.pause == False:
            self._stop()
            self.pause = True
        else:
            self._start()
            self.pause = False

    @property
    def take_photo(self):
        file_name = './temp/{}.png'.format(time.time())
        cv2.cv.SaveImage(file_name, self.frame)
        return file_name

    # @property
    def _get_frame(self):
        self.frame = cv2.cv.QueryFrame(self._camera)
        # print self.frame
        self.update()
        # return self.frame

    def paintEvent(self, QPaintEvent):
        if self.frame is None:
            return
        painter = QtGui.QPainter(self)
        painter.drawImage(QtCore.QPoint(0, 0), OpenCVtoPyQt(self.frame))


class PushButton(QtGui.QWidget):

    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)
        self.init()

    def init(self):
        layout = QtGui.QHBoxLayout(self)
        self.take_photo = QtGui.QPushButton(self)
        self.take_photo.setText('photo')
        self.take_photo.clicked.connect(self._take_photo)

        self.start = QtGui.QPushButton(self)
        self.start.setText('start')
        self.start.clicked.connect(self._start)

        self.pause = QtGui.QPushButton(self)
        self.pause.setText('pause')
        self.pause.clicked.connect(self._pause)

        layout.addStretch(1)
        layout.addWidget(self.take_photo)
        layout.addWidget(self.start)
        layout.addWidget(self.pause)
        layout.addStretch(1)
        self.setLayout(layout)

    def _start(self):
        self.parent().parent().parent().left.up._start()
        # pass

    def _pause(self):
        self.parent().parent().parent().left.up._pause()
        # pass

    def _take_photo(self):
        file_name = self.parent().parent().parent().left.up.take_photo
        self.parent().parent().parent().right._open(file_name)
        # print self.parent().up


class Combine(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Combine, self).__init__(parent)
        self.init()

    def init(self):
        # layout = QtGui.QVBoxLayout(self)
        # layout.addWidget(CameraWidget(self))
        # layout.addWidget(PushButton(self))
        # self.setLayout(layout)
        self.split = QtGui.QSplitter(QtCore.Qt.Vertical, self.parent())
        self.up = CameraWidget(self.split)
        self.down = PushButton(self.split)
        self.split.setStretchFactor(0, 1)
        # self.split.setStretchFactor(1, 1)
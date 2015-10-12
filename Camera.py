__author__ = 'KDQ'

from PyQt4 import QtGui
from PyQt4 import QtCore
import cv2
import time

class OpenCVtoPyQt(QtGui.QImage):

    def __init__(self, opencvImg):
        depth, nchannel = opencvImg.depth, opencvImg.nChannels
        w, h = cv2.cv.GetSize(opencvImg)
        frame1 = cv2.cv.CreateImage((w, h), depth, nchannel)
        cv2.cv.CvtColor(opencvImg, frame1, cv2.cv.CV_BGR2RGB)
        self._imgData = frame1.tostring()
        super(OpenCVtoPyQt, self).__init__(self._imgData, w, h, QtGui.QImage)


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

    def take_photo(self):
        file_name = './temp/{}.png'.format(time.time())
        cv2.imwrite(file_name, self.frame)
        self.parent().right._open(file_name)

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


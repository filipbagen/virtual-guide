from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
import cv2

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(QImage)

    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self._run_flag = True
        self.width = width
        self.height = height

    def run(self):
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        vid = cv2.VideoCapture(0)
        vid.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        vid.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        while self._run_flag:
            ret, frame = vid.read()
            if ret:
                imagetemp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                opencv_image = cv2.flip(imagetemp, 1)
                faces = faceCascade.detectMultiScale(opencv_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                for (x, y, w, h) in faces:
                    center = (x + w//2, y + h//2)
                    radius = w//2
                    cv2.circle(opencv_image, center, radius, (0, 0, 0), 2)

                rgb_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
               
                self.change_pixmap_signal.emit(qt_image)
            else:
                break
        
        vid.release()
        cv2.destroyAllWindows()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

class VideoWidget(QWidget):
    def __init__(self, parent=None):
        super(VideoWidget, self).__init__(parent)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 640, 480)

        self.thread = VideoThread(640, 480)
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    def update_image(self, img):
        self.label.setPixmap(QPixmap.fromImage(img))


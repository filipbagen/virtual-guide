from PyQt6.QtGui import QColor, QPainter, QBrush, QPen
from PyQt6.QtCore import Qt, QTimer, QRect
from PyQt6.QtWidgets import QApplication, QWidget
import cv2
import sys

class HeadWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)

        self.head_size = 70
        self.head_x = (self.width() - self.head_size) // 2
        self.head_y = (self.height() - self.head_size) // 2

        self.Eyes_size = 200
        self.Eyes_x = (self.width() - self.Eyes_size) // 4
        self.Eyes_y = (self.height() - self.Eyes_size) // 4

        self.setStyleSheet("background-color: black;")
        self.update_head_position()

        timer = QTimer(self)
        timer.timeout.connect(self.update_head_position)
        timer.start(50)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setPen(QPen(QColor(0, 0, 0), 12, Qt.PenStyle.SolidLine))

        painter.setBrush(QBrush(QColor(30, 144, 255), Qt.BrushStyle.SolidPattern))
        painter.drawEllipse(QRect(self.Eyes_x, self.Eyes_y, self.Eyes_size, self.Eyes_size))
        painter.drawEllipse(QRect(self.Eyes_x + self.Eyes_size + 50, self.Eyes_y, self.Eyes_size, self.Eyes_size))

        painter.setBrush(QBrush(QColor(255, 255, 255), Qt.BrushStyle.SolidPattern))
        painter.drawEllipse(QRect(self.head_x, self.head_y, self.head_size, self.head_size))
        painter.drawEllipse(QRect(self.head_x + self.head_size + 150, self.head_y, self.head_size, self.head_size))

    def get_head_position(self):
        ret, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            return x, y

        return self.get_head_position()

    def update_head_position(self):
        self.head_x, self.head_y = self.get_head_position()

        x_min = self.Eyes_x + self.head_size // 2
        x_max = self.Eyes_x + self.Eyes_size - self.head_size // 2
        y_min = self.Eyes_y + self.head_size // 2
        y_max = self.Eyes_y + self.Eyes_size - self.head_size // 2

        self.head_x = max(min(self.head_x, x_max), x_min)
        self.head_y = max(min(self.head_y, y_max), y_min)

        pupil_offset = self.head_size // 2
        pupil_x = self.head_x + pupil_offset
        pupil_y = self.head_y + pupil_offset
        if pupil_x + pupil_offset > self.Eyes_x + self.Eyes_size:
            pupil_x = self.Eyes_x + self.Eyes_size - pupil_offset
        elif pupil_x - pupil_offset < self.Eyes_x:
            pupil_x = self.Eyes_x + pupil_offset
        if pupil_y + pupil_offset > self.Eyes_y + self.Eyes_size:
            pupil_y = self.Eyes_y + self.Eyes_size - pupil_offset
        elif pupil_y - pupil_offset < self.Eyes_y:
            pupil_y = self.Eyes_y + pupil_offset

        self.head_x = pupil_x - pupil_offset
        self.head_y = pupil_y - pupil_offset

        self.update()
        
   


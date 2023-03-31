from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, pyqtSignal

from speech_recognition import speech_rec
from chat_bot import generate_text
from text_to_speech import talk

from ImageAnlysis import VideoWidget

class ConversationThread(QThread):
    input_signal = pyqtSignal(str)
    output_signal = pyqtSignal(str)

    def run(self):
        while True:
            input = speech_rec()
            self.input_signal.emit(input)
            
            output = generate_text(input)
            self.output_signal.emit(output)
            
            talk(output)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.width, self.height = 1500, 800

        self.setWindowTitle("Virtual Guide")
        self.resize(self.width, self.height)

        self.label = QLabel(self)
        self.label.setText("Hello, I'm your Virtual Guide")
        self.label.setStyleSheet("color: white; font-size: 40px;")
        self.label.setGeometry(100, 20, 600, 60)

        self.canvas = QLabel(self)
        self.canvas.setGeometry(700, 140, 780, 620)

        self.textBoxInput = QTextEdit(self)
        self.textBoxInput.setGeometry(100, 140, 500, 150)

        self.textBoxOutput = QTextEdit(self)
        self.textBoxOutput.setGeometry(100, 300, 500, 150)

        self.video_widget = VideoWidget(self)
        self.video_widget.setGeometry(700, 140, 780, 620)
        

        self.buttonStart = QPushButton("START CONVERSATION", self)
        self.buttonStart.setGeometry(100, 500, 200, 100)
        self.buttonStart.clicked.connect(self.on_button_clicked)

        self.conversation_thread = ConversationThread()
        self.conversation_thread.input_signal.connect(self.set_input_text)
        self.conversation_thread.output_signal.connect(self.set_output_text)

    def set_input_text(self, text):
        self.textBoxInput.setText(text)

    def set_output_text(self, text):
        self.textBoxOutput.setText(text)

    def on_button_clicked(self):
        if not self.conversation_thread.isRunning():
            self.conversation_thread.start()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

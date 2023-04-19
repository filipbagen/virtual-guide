from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QDesktopWidget
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

        self.setWindowTitle("VIRTUAL GUIDE")
        self.resize(self.width, self.height)
        self.setStyleSheet("background-color: #DEDEDE;")

        # Get screen resolution
        screen_resolution = QDesktopWidget().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        
        # Set label geometry
        self.label = QLabel(self)
        self.label.setText("Hello, I'm your Virtual Guide. Say Hi or click the button to start the conversation.")
        self.label.setStyleSheet("color: black; font-size: 35px; font-weight: bold; font-family: Helvetica;")
        self.label.setGeometry((width - 1350) // 2, height // 8, 1350, 120)

        # Set canvas geometry
        self.canvas = QLabel(self)
        self.canvas.setGeometry((width - 780) // 2, height // 4, 780, 620)

        # Set text box geometry
        self.textBoxInput = QTextEdit(self)
        self.textBoxInput.setGeometry(600, (height // 2.5) -200, 700, 500)
        self.textBoxInput.setReadOnly(True)
        self.textBoxInput.setStyleSheet("""
        QWidget {
            background-color: #DEDEDE;
            border: 1px solid #DEDEDE;
            color: black; 
            font-size: 20px; 
            font-weight: bold; 
            font-family: Helvetica;
            }
        """)
        
        # Set button geometry
        self.buttonStart = QPushButton("START CONVERSATION", self)
        self.buttonStart.setGeometry(850, 800, 200, 50)
        self.buttonStart.clicked.connect(self.on_button_clicked)
        self.buttonStart.setStyleSheet("""
        QPushButton {
            color: #fff;
            background-color: #0d6efd;
            border-color: #0d6efd;
            font-weight: 400;
            line-height: 1.5;
            text-align: center;
            border: 1px solid transparent;
            padding: 6px 12px;
            font-size: 16px;
            border-radius: .25rem;
            }
        """)
        
        self.buttonStop = QPushButton("STOP CONVERSATION", self)
        self.buttonStop.setGeometry(600, 800, 200, 50)
        self.buttonStop.clicked.connect(self.on_button_stop_clicked)
        self.buttonStop.setStyleSheet("""
        QPushButton {
            color: #fff;
            background-color: #dc3545;
            border-color: #dc3545;
            font-weight: 400;
            line-height: 1.5;
            text-align: center;
            border: 1px solid transparent;
            padding: 6px 12px;
            font-size: 16px;
            border-radius: .25rem;
            }
        """)

        self.conversation_thread = ConversationThread()
        self.conversation_thread.input_signal.connect(self.set_text)

    def set_text(self, text):
        self.textBoxInput.append(text)
        self.textBoxoutput.append(text)

    def on_button_clicked(self):
        self.textBoxInput.setText(self.textBoxInput.toPlainText() + "\n\nConversation started, I'am listening..\n\n")
        if not self.conversation_thread.isRunning():
            self.conversation_thread.start()
            
    def on_button_stop_clicked(self):
        self.textBoxInput.setText(self.textBoxInput.toPlainText() + "\n\nConversation ended, I have stopped listening.\n\n")
        if self.conversation_thread.isRunning():
            self.conversation_thread.terminate()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

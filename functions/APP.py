import cv2
from PyQt6.QtGui import (
    QPixmap, 
    QTextCursor, 
    QTextCharFormat, 
    QColor
) 
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QPlainTextEdit,
    QSizePolicy
)
from PyQt6.QtCore import (
    QPropertyAnimation, 
    QSequentialAnimationGroup, 
    QPoint, 
    QSize, 
    Qt,
    QThread, 
    pyqtSignal, 
    pyqtSlot
)
from PyQt6.QtGui import QColor, QPainter, QBrush, QPen
from PyQt6.QtCore import Qt, QTimer

from speechrec import speech_rec
from T5 import get_answer
from text_to_speech import talk
import speech_recognition as sr

counter = 0

class ConversationThread(QThread):
    update_gui_signal = pyqtSignal(str)

    def run(self):    
        r = sr.Recognizer()

        while True:
            with sr.Microphone() as source:
                audio = r.listen(source)

            try:
                input_text = r.recognize_google(audio)
                self.update_gui_signal.emit(input_text)

                if "hello" or "hey" or "hi" in input_text.lower():
                    output_text = "Hello, I'm your Virtual Guide. How can I help you today?"
                    self.update_gui_signal.emit(output_text)
                    talk(output_text)
                  
                    while True:
                        input_text = speech_rec()
                        self.update_gui_signal.emit(input_text)
                        output_text = get_answer(input_text)
                        self.update_gui_signal.emit(output_text)
                        talk(output_text)
                        
                else:
                    output_text = "Please say 'hello' to start the conversation."
                    self.update_gui_signal.emit(output_text)

            except sr.UnknownValueError:
                output_text = "Sorry, I didn't understand what you said."
                self.update_gui_signal.emit(output_text)
            except sr.RequestError:
                output_text = "Sorry, there was an error processing your request."
                self.update_gui_signal.emit(output_text)
    
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Virtual Guide")
        self.setStyleSheet(
            """
                background-color: #4d4f5c;
            """)

        label = QLabel("Hello, I'm your Virtual Guide.")
        label.setStyleSheet(
            """
                color: #DEDEDE;
                font-size: 25px;
                font-family: Helvetica;
                font-weight: bold;
                text-align: center;
            """)

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(0, 0, self.width(), self.height())

        self.textEditInput = QTextEdit()
        self.textEditInput.setReadOnly(True)
        self.textEditInput.setMinimumSize(500, 500)
        self.textEditInput.setStyleSheet(
            """
                QTextEdit {
                    background-color: white;
                    border-radius: 10px;
                    font-family: Helvetica;
                }
            """)

        placeholderbot = QLabel("hej")
        placeholderbot.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        placeholderbot.setMinimumSize(500, 500)
        placeholderbot.setStyleSheet("""
                background-color: white;
                border-radius: 10px;
            """)

        appContainer = QHBoxLayout(self)
        botContainer = QVBoxLayout(self)
        chatContainer = QVBoxLayout(self)
        buttonContainer = QHBoxLayout()
        chatContainer.addWidget(self.textEditInput)        
        buttonContainer.addWidget(self.buttonStart())
        buttonContainer.addWidget(self.buttonStop())
        botContainer.addWidget(label)
        botContainer.addWidget(placeholderbot)
        botContainer.addLayout(buttonContainer)
        appContainer.addLayout(botContainer)
        appContainer.addLayout(chatContainer)

        self.conversation_thread = ConversationThread()
        self.conversation_thread.update_gui_signal.connect(self.set_text)
        
    def set_text(self, text):
        global counter
        
        if (counter % 2) == 0:
            self.textEditInput.insertHtml("<div style='font-size: 20px; color: white; background-color: #1e90ff; padding: 20px; vertical-align:middle; '>{}</div><br />".format(text))
        else: 
            self.textEditInput.insertHtml("<div style='font-size: 20px; color: black; background-color: white; padding: 20px; vertical-align:middle; '>{}</div><br />".format(text))
        counter += 1

    def buttonStop(self):
        button = QPushButton("KILL ME", self)
        button.setFixedSize(250, 50)
        button.clicked.connect(QApplication.quit)
        button.setStyleSheet("""
            QPushButton {
                background-color: #1e90ff;
                color: white;
                font-family: Helvetica;
                border-radius : 10;
                border : 5px solid #1e90ff;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """)

        return button

    def buttonStart(self):
        button = QPushButton("START LISTENING", self)
        button.setFixedSize(250, 50)
        button.clicked.connect(self.on_button_start_clicked)
        button.setStyleSheet(""" 
            QPushButton {
                background-color: #1e90ff;
                color: white; 
                font-family: Helvetica;
                border-radius : 10; 
                border : 5px solid #1e90ff;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                text-decoration: underline;
            } 
        """)
        return button

    def on_button_start_clicked(self):
        self.textEditInput.insertHtml("<div style='font-size: 20px; color: white; background-color: #1e90ff; padding: 20px; vertical-align: middle;'>{}</div><br />".format("I am listening..."))
        if not self.conversation_thread.isRunning():
            self.conversation_thread.start()
            
    def on_hello(self):
        self.textEditInput.setText(self.textEditInput.toPlainText() + "\n\nHello, starting conversation..\n\n")
        if not self.conversation_thread.isRunning():
            self.conversation_thread.start()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

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

from speech_recognition import speech_rec
# from chat_bot import generate_text
from T5 import get_answer
from text_to_speech import talk
# from ImageAnlysis import VideoWidget

counter = 0
context = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."

class ConversationThread(QThread):
    update_gui_signal = pyqtSignal(str)

    def run(self):
        while True:
            input_text = speech_rec()
            self.update_gui_signal.emit(input_text)
            output_text = get_answer(input_text, context)
            self.update_gui_signal.emit(output_text)
            talk(output_text)
    
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
        button = QPushButton("START CONVERSATION", self)
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

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

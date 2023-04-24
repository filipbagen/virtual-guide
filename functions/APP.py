from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
from speech_recognition import speech_rec
from chat_bot import generate_text
from text_to_speech import talk


class ConversationThread(QThread):
    input_signal = pyqtSignal(str)
    output_signal = pyqtSignal(str)
    update_gui_signal = pyqtSignal(str)

    def run(self):
        while True:
            input_text = speech_rec()
            self.update_gui_signal.emit(input_text)
            output_text = generate_text(input_text)
            self.update_gui_signal.emit(output_text)
            talk(output_text)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VIRTUAL GUIDE")
        self.setStyleSheet("background-color: #DEDEDE;")
        
        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()

        label = QLabel(
            "Hello, I'm your Virtual Guide. Say Hi or click the button to start the conversation."
        )
        label.setStyleSheet(
            "color: black; font-size: 25px; font-weight: bold; font-family: Helvetica;"
        )
        label.setFixedWidth(1000)
        label.setAlignment(Qt.AlignCenter)
        
        self.textEditInput = QTextEdit()
        self.textEditInput.setReadOnly(True)
        self.textEditInput.setStyleSheet(
            """
            QTextEdit {
                background-color: #DEDEDE;
                border: 1px solid #DEDEDE;
                color: black;
                font-size: 20px;
                font-weight: bold;
                font-family: Helvetica;
            }
        """
        )

        buttonStart = QPushButton("START CONVERSATION")
        buttonStart.setFixedWidth(200)
        buttonStart.clicked.connect(self.on_button_start_clicked)
        buttonStart.setStyleSheet(
            """
            QPushButton {
                color: #fff;
                background-color: #0d6efd;
                border-color: #0d6efd;
                font-weight: 400;
                line-height: 1.5;
                text-align: center;
                border: 1px solid transparent;
                padding: 12px;
                font-size: 16px;
                border-radius: .25rem;
            }
        """
        )

        buttonStop = QPushButton("KILL PROGRAM")
        buttonStop.setFixedWidth(200)
        buttonStop.clicked.connect(self.on_button_stop_clicked)
        buttonStop.setStyleSheet(
            """
            QPushButton {
                color: #fff;
                background-color: #dc3545;
                border-color: #dc3545;
                font-weight: 400;
                line-height: 1.5;
                text-align: center;
                border: 1px solid transparent;
                padding: 12px;
                font-size: 16px;
                border-radius: .25rem;

            }
        """
        )

        vbox.addWidget(label)
        
        vbox.addWidget(self.textEditInput)
        
        hbox.addWidget(buttonStart)
        hbox.addWidget(buttonStop)
        vbox.addLayout(hbox)

        self.conversation_thread = ConversationThread()
        self.conversation_thread.update_gui_signal.connect(self.set_text)
        
    def on_button_start_clicked(self):
        self.textEditInput.setText(self.textEditInput.toPlainText() + "\n\nConversation started, I'm listening..\n\n")
        if not self.conversation_thread.isRunning():
            self.conversation_thread.start()
    
    @pyqtSlot(str)
    def update_text(self, text):
        self.textEditInput.append(text)
        
    def on_button_stop_clicked(self):
        self.textEditInput.setText(self.textEditInput.toPlainText() + "\n\nConversation ended, closing down.\n\n")
        QApplication.quit()
    
    def set_text(self, text):
        self.textEditInput.append(text)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



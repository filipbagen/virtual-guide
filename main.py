# from tkinter import *
# from functions.gui import gui

# app = Tk()
# gui(app)
# app.mainloop()

from functions.speech_recognition import speech_rec
from functions.chat_bot import generate_text
from functions.text_to_speech import talk

input = speech_rec()
output = generate_text(input)
talk(output)

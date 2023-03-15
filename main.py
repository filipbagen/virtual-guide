from tkinter import *
import cv2
from PIL import Image, ImageTk
import whisper
import sounddevice
from scipy.io.wavfile import write 
from gtts import gTTS
from playsound import playsound
import os

vid = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

width, height = 1500, 800

vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

app = Tk()

label = Label(
    text="Hello, I'am your Virtual Guide",
    foreground="white", 
    background="black"  
)
label.pack()

app.bind('<Escape>', lambda e: app.quit())

label_widget = Label(app)
label_widget.pack()

canvas = Canvas(app, width=width, height=height)
canvas.pack()

def draw_box(x, y, w, h):
    canvas.delete("all")
    canvas.create_oval(x, y, x+w, y+h, fill='white', width=3, outline='white')
    image = Image.open("smiley.png")
    image = image.resize((int(w), int(h)))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(x + w/2, y + h/2, image=photo)
    canvas.image = photo

def open_camera():
    _, frame = vid.read()
    imagetemp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    opencv_image = cv2.flip(imagetemp, 1)
    
    faces = faceCascade.detectMultiScale(opencv_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        draw_box(x, y, w, h)
    
    captured_image = Image.fromarray(opencv_image)
    photo_image = ImageTk.PhotoImage(image=captured_image)
    label_widget.photo_image = photo_image
    label_widget.after(10, open_camera)
    
def talk(text): 
    tts = gTTS(text=text, lang='sv', slow=False)

    tts.save("tts.mp3")
    
    path = os.path.abspath("tts.mp3")
    playsound(path)
    
button = Button(
    text="START",
    width=25,
    height=5,
    bg="white",
    fg="black",
    command=open_camera
)
button.pack()

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    talk(inputValue)

textBox=Text(app, height=200, width=100)
textBox.pack()
    
buttonCommit=Button(app, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())

buttonCommit.pack()

app.mainloop()
vid.release()

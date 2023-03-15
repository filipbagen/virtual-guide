from tkinter import *
import cv2
from PIL import Image, ImageTk
import time

def draw_box(x, y, w, h, canvas,vid):
    
    canvas.delete("all")
    canvas.create_oval(x, y, x+w, y+h, fill='white', width=3, outline='white')
    image = Image.open("smiley.png")
    image = image.resize((int(w), int(h)))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(x + w/2, y + h/2, image=photo)
    canvas.image = photo
    
    canvas.pack()
    vid.release()

def open_camera(canvas,label_widget,width, height):
    
    vid = cv2.VideoCapture(0)
    
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    _, frame = vid.read()
    
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    imagetemp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    opencv_image = cv2.flip(imagetemp, 1)

    faces = faceCascade.detectMultiScale(opencv_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        draw_box(x, y, w, h, canvas, vid)

    captured_image = Image.fromarray(opencv_image)
    photo_image = ImageTk.PhotoImage(image=captured_image)
    label_widget.photo_image = photo_image
    
    label_widget.after(10, open_camera, canvas, label_widget, width, height)
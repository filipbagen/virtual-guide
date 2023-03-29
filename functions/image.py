from tkinter import *
import cv2
from PIL import Image, ImageTk
import threading

def draw_box(x, y, w, h, canvas, vid):
    canvas.delete("all")
    canvas.create_oval(x, y, x+w, y+h, fill='white', width=3, outline='white')
    canvas.update()
    
    # img= ImageTk.PhotoImage(Image.open("smiley.png"))
    # canvas.create_image(5, 5, anchor=NW, image=img)
    # canvas.img_tk = img

def open_camera(canvas,label_widget,width, height):
    vid = cv2.VideoCapture(0)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def process_video():
        while True:
            _, frame = vid.read()
            faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            imagetemp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            opencv_image = cv2.flip(imagetemp, 1)
            faces = faceCascade.detectMultiScale(opencv_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                draw_box(x, y, w, h, canvas, vid)
            

    t = threading.Thread(target=process_video)
    t.daemon = True
    t.start()
    
    
    
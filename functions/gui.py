from tkinter import *
from functions.image import open_camera
from functions.talk import talk
from functions.talk import listen

def gui(app): 
    
    width, height = 1500, 800
    
    canvas = Canvas(app, width=width, height=height)
    canvas.pack()

    label_widget = Label(app)
    label_widget.pack()
    
    def retrieve_input():
        inputValue=textBox.get("1.0","end-1c")
        talk(inputValue)

    label = Label(
        app,
        text="Hello, I'am your Virtual Guide",
        foreground="white", 
        font=("Helvetica", 40)
    )
    label.pack(side=TOP, anchor=N)

    textBox=Text(
        app,
        height=10, 
        width=50,
        )
    textBox.pack()
    textBox.place(x=100, y=140)
        
    buttonCommit=Button(
        app,
        width=25,
        height=5,
        text="SEND TEXT PROMPT", 
        command=lambda: retrieve_input()
        )
    buttonCommit.pack()
    buttonCommit.place(x=100, y=300)

    buttonCamera = Button(
        text="START CAMERA FEED",
        width=25,
        height=5,
        bg="white",
        fg="black",
        command=lambda: open_camera(canvas,label_widget,width, height)

        )
    buttonCamera.pack()
    buttonCamera.place(x=100, y=400)
    
    buttonListen = Button(
        text="START WHISPER FEED",
        width=25,
        height=5,
        bg="white",
        fg="black",
        command=lambda: listen()

        )
    buttonListen.pack()
    buttonListen.place(x=100, y=500)


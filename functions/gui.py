from tkinter import *
from functions.image import open_camera
from functions.talk import talk
from functions.talk import speech_to_text

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
        text="Hello, I'm your Virtual Guide",
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
        text="SEND TEXT PROMPT TO BE READ", 
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
        text="START SPEECH TO TEXT FEED",
        width=25,
        height=5,
        bg="white",
        fg="black",
        command=lambda: retrieve_input2()
        )
    buttonListen.pack()
    buttonListen.place(x=100, y=500)

    textBox2=Text(
            app,
            height=10, 
            width=50,
            )
    textBox2.pack()
    textBox2.place(x=100, y=610)

    def retrieve_input2():
        text = speech_to_text() 
        textBox2.insert(END, text)
        
    buttonListenAndTalk = Button(
        text="START SPEECH TO SPEECH FEED",
        width=25,
        height=5,
        bg="white",
        fg="black",
        command=lambda: retrieve_input3()
        )
    buttonListenAndTalk.pack()
    buttonListenAndTalk.place(x=100, y=760)
    
    def retrieve_input3():
        text = speech_to_text() 
        talk(text)
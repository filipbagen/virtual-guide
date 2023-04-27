import numpy as np
from scipy.io import wavfile 
from numpy import fft as fft
import time
import tkinter as tk
import threading
import pyaudio
import wave

CHUNK = 1024
wf = wave.open("test3.wav", 'rb') #behöver vara wav fil om vi ska få ut amplitud
p = pyaudio.PyAudio()

###
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

####

rate,audData = wavfile.read("test3.wav")

print ("Rate "+str(rate))
print ("Length of wav file(in s) = " + str(audData.shape[0]/rate))

ch1=audData[:]
tim = 0.050
pt=int(tim*rate)

flag2 = True
flag = False
cnt = 0
value=0

def bass():
    global pt
    global cnt
    global audData
    global value
    global flag2
    global flag

    cnt +=1
    fourier=fft.fft(ch1[((cnt-1)*pt):((cnt)*pt)])
    fourier = abs(fourier) / float(pt)
    fourier = fourier[0:25]
    fourier = fourier**2

    if (cnt+1)*pt > len(audData[:]) :
        flag2 = False

    value = (np.sum(fourier))/pt
    flag= True
    return

def plot():
    global value
    global flag

    root=tk.Tk()

    canvas =tk.Canvas(root,width=200,height=500)
    canvas.pack()

    while True:
        if flag:
            canvas.delete("all")
            flag=False
            greenbox = canvas.create_rectangle(50,500-(value/2),150,500,fill="green")
            print(value/2) # Check if it is over 500
        root.update_idletasks()    
        root.update()

    return

def sound():
    global data
    global stream
    global wf
    global CHUNK

    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()
    p.terminate()


bass()
t1 = threading.Thread(target=plot, name='t_1')
t2 = threading.Thread(target=sound, name='t_2')
t1.start()
t2.start()

while flag2:
    a = time.time()
    bass()
    b=time.time()
    while (b-a) < tim :
        time.sleep(0.015)
        b=time.time()
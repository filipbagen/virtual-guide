from FaceTrack.FaceTrack import *
from Sound.speech_to_text import *

#for a in face_track():
  
face = False
temp = False 
  
for face in face_track(): 
    if face == True:
        result = speech_to_text()
        print(result["text"])
            
        
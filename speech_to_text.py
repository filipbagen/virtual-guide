import whisper
import sounddevice
from scipy.io.wavfile import write 

sr=44100
seconds=3
print('Recording\n')
record_voice=sounddevice.rec(sr*seconds, samplerate=sr, channels=1) 
sounddevice.wait()
write('audio.mp3',sr,record_voice)


model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
print('Finished')
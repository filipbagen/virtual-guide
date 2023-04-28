from TTS.api import TTS
import io
import numpy as np
import pyaudio
import wave

tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")

def talk(text):
    audio_samples = tts.tts(text)
    max_amplitude = np.abs(audio_samples).max()
    scaled_samples = np.int16(audio_samples / max_amplitude * 32767)

    CHUNK = 1024

    with io.BytesIO() as f:
        wf = wave.open(f, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(22050)
        wf.writeframes(scaled_samples.tobytes())
        wf.close()

        f.seek(0)
        wf = wave.open(f, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)

        while data:
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()

        p.terminate()
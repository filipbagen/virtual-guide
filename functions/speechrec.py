# import whisper
# import sounddevice
# from scipy.io.wavfile import write
# import os

# model = whisper.load_model("base.en")


# def speech_rec():
#     sr = 44100
#     seconds = 4
#     print('Recording\n')
#     record_voice = sounddevice.rec(sr * seconds, samplerate=sr, channels=1)
#     sounddevice.wait()
#     write('audio.mp3', sr, record_voice)

#     result = model.transcribe('audio.mp3')
#     os.remove('audio.mp3')
#     print('Finished')

#     return result["text"]

import whisper
import speech_recognition as sr
import os

# Create a recognizer object and wake word variables
recognizer = sr.Recognizer()
WAKE_WORD = "hello"


def speech_rec():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        # print(f"Waiting for wake words 'ok bing' or 'ok chat'...")

        # while True:
        #     # Listen for "hello"
        #     audio = recognizer.listen(source)
        #     try:
        #         with open("audio.wav", "wb") as f:
        #             f.write(audio.get_wav_data())
        #         # Use the preloaded tiny_model
        #         model = whisper.load_model("tiny")
        #         result = model.transcribe("audio.wav")
        #         phrase = result["text"]
        #         print(f"You said: {phrase}")

        #         wake_word = get_wake_word(phrase)
        #         if wake_word is not None:
        #             break
        #         else:
        #             print("Not a wake word. Try again.")

        #     except Exception as e:
        #         print("Error transcribing audio: {0}".format(e))
        #         continue

        # print("Speak a prompt...")
        audio = recognizer.listen(source)

        try:
            # Transcribe the question
            with open("audio_prompt.wav", "wb") as f:
                f.write(audio.get_wav_data())
            model = whisper.load_model("base.en")
            result = model.transcribe(
                "audio_prompt.wav", fp16=False, language="English"
            )
            user_input = result["text"]
            os.remove("audio_prompt.wav")
            return user_input

        except Exception as e:
            print("Error transcribing audio: {0}".format(e))

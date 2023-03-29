import speech_recognition
import pyttsx3

def speech_to_text():

    recognizer = speech_recognition.Recognizer()

    while True:

        try:

            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio, language="sv-SE")
                text = text.lower()

                print(f"{text}")
                return text

        except speech_recognition.UnknownValueError:
            print("Could not understand audio")
            
speech_to_text()
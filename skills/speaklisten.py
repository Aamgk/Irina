import speech_recognition as sr
import pyttsx3

class SpeakListen:
    def __init__(self):
        self.speech_engine = pyttsx3.init()
        voices = self.speech_engine.getProperty('voices')
        for voice in voices:
             if voice.id == 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0':
                  self.speech_engine.setProperty('voice', voice.id)
        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index=0)
    
    def speak(self, text):
        self.speech_engine.say(text, "speech")
        self.speech_engine.runAndWait()


    def listen(self):
        try:
            with self.mic as source:
                print("Listening")
                self.r.non_speaking_duration = 0.5
                audio = self.r.listen(source, timeout=7, phrase_time_limit=5)
            return (self.r.recognize_google(audio, language="ru-RU"))
        except sr.exceptions.UnknownValueError:
            self.speech_engine.say("Простите, я вас не поняла")


    
# speaklisten = SpeakListen()
# # # print(speaklisten.listen())
# speaklisten.speak('как дела?')
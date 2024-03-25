import speech_recognition as sr
import pyttsx4


class SpeechServices:
    talk_engine = pyttsx4.init()
    recognition_engine = sr.Recognizer()

    def talk(self, msg):
        self.talk_engine.say(msg)
        self.talk_engine.runAndWait()

    def say(self, msg):
        self.talk(msg)

    def listen(self):
        with sr.Microphone() as source:
            audio = self.recognition_engine.listen(source)

            return self.recognition_engine.recognize_whisper(
                audio,
                language='turkish')

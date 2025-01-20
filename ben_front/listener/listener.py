import speech_recognition as sr

from PyCoink import pycoink

ACTIVATION_PHRASE: str = "hey"

class Listener:
    def __init__(self):
        self.rec = sr.Recognizer()
        self.transcript: str = ""


    def start(self) -> None:
        while self.transcript == "":
            text = self._listen()
            if not ACTIVATION_PHRASE in text.lower():
                continue
            self.transcript = text
    

    def _listen(self) -> str:
        with sr.Microphone() as source:
            pycoink.Log.info("Adjusting for ambient noise... Please wait")
            self.rec.adjust_for_ambient_noise(source, duration=1)
            pycoink.Log.info("Listening... Please speak now.")

            try:
                # Capture audio from the microphone
                audio = self.rec.listen(source, timeout=5)
                pycoink.Log.info("Processing your speech...")

                # Use Google Web Speech API for transcription
                transcript = self.rec.recognize_google(audio)
                pycoink.Log.info("You said:", transcript)
                return transcript

            except sr.WaitTimeoutError:
                pycoink.Log.error("No speech detected. Please try again.")
            except sr.UnknownValueError:
                pycoink.Log.error("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
                pycoink.Log.error("Could not request results", e)
        
        return ""

import speech_recognition as sr

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

    def extract_transcript(self) -> str:
        ret: str = self.transcript.strip().lower()
        self.transcript = ""    
        return ret
    

    def _listen(self) -> str:
        with sr.Microphone() as source:
            print("[ INFO] Adjusting for ambient noise... Please wait")
            self.rec.adjust_for_ambient_noise(source, duration=1)
            print("[ INFO] Listening... Please speak now.")

            try:
                # Capture audio from the microphone
                audio = self.rec.listen(source, timeout=5)
                print("[ INFO] Processing your speech...")

                # Use Google Web Speech API for transcription
                transcript = self.rec.recognize_google(audio)
                print("[ INFO] You said:", transcript)
                return transcript

            except sr.WaitTimeoutError:
                print("[ERROR] No speech detected. Please try again.")
            except sr.UnknownValueError:
                print("[ERROR] Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
                print("[ERROR] Could not request results", e)
        
        return ""

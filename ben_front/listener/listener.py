import speech_recognition as sr


class Listener:
    def __init__(self):
        self.rec = sr.Recognizer()


    def listen(self) -> str:
        text = ""
        while text == "":
            text = self._listen()
        return text.strip().lower()
    

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

import multiprocessing
import threading
import requests
import time
import pyttsx3 # text to speech

from listener.listener import Listener
from monitor.monitor import Monitor

URL = "http://127.0.0.1:5555/api"
ENDPOINT_ASK = "/ask"
ENDPOINT_ANS = "/answer"
HEADERS = {"Content-Type": "text/plain"}

class Kernel:
    def __init__(self):
        self.listener = Listener()
        self.lock = threading.Lock()

        self.transcript = ""
        self.monitor = None


    def run(self) -> None:
        while True:
            # Wait for something to be said
            self.transcript = self.listener.listen()
            if not "hey" in self.transcript:
                self.transcript = ""  # Cancel transcript if it doesn't contain activation key
                continue

            # Send transcript to back-end server
            t1 = threading.Thread(target=self._request_thread)
            t1.start()

            # Start the monitor on first interaction
            if self.monitor is None:
                self.monitor = Monitor()
                self.monitor.start()

            # Ensure thread completion
            t1.join()

    
    def _request_thread(self, listen = False) -> None:
        time.sleep(1)

        copy_tr = ""

        if listen:
            while self.transcript == "":
                self.transcript = self.listener.listen()
            self.lock.acquire()
            copy_tr += self.transcript
            self.transcript = ""
            self.monitor.user_message(copy_tr)
            self.lock.release()
        else:
            self.lock.acquire()
            copy_tr += self.transcript # copyr transcript
            self.transcript = ""
            self.monitor.user_message(copy_tr)
            self.lock.release()

        if "exit" in copy_tr:
            self.lock.acquire()
            self.monitor.stop()
            self.monitor = None
            self.lock.release()
            return

        # send transcript to back
        print("Sending '", copy_tr, "' to ",  URL + ENDPOINT_ASK , " ...")
        response = requests.post(
            URL + ENDPOINT_ASK,
            data=copy_tr,
            headers=HEADERS
        )

        if response.status_code != 200:
            print("[ERROR] ", response.json())
            return
        
        response_data = response.json()["data"]
        answer: str = response_data["transcript"]
        print(f"[DEBUG] Server answer is : '{answer}'")
                
        # send answer to monitor
        self.lock.acquire()
        self.monitor.ben_message(answer)
        self.lock.release()

        # TTS in a non-blocking manner using a new process
        tts_process = multiprocessing.Process(target=self._speak, args=(answer,))
        tts_process.start()
        tts_process.join()


        # Start listening again
        print("[ INFO] Ready to listen again...")
        self._request_thread(listen=True)


    @staticmethod
    def _speak(text: str):
        try:
            tts = pyttsx3.init()
            tts.say(text)
            tts.runAndWait()  # Blocks until TTS finishes
        except Exception as e:
            print(f"[ERROR] TTS failed: {e}")
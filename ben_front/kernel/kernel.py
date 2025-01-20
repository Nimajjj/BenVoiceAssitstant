import threading
import requests

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


    def start(self) -> None:
        # wait for something to be said
        self.listener.start()
        
        # send transcript to back end server
        self.t1 = threading.Thread(target=self._request_thread)
        self.t1.start()

        # start monitor
        transcript: str = self.listener.transcript
        self.monitor = Monitor()        
        self.monitor.start(transcript)

        # get back thread
        self.t1.join()

    
    def _request_thread(self) -> None:
        # send transcript to back
        print("Sending '", self.listener.transcript, "' to ",  URL + ENDPOINT_ASK , " ...")
        
        self.lock.acquire()
        data = self.listener.transcript
        self.lock.release()

        response = requests.post(
            URL + ENDPOINT_ASK,
            data=data,
            headers=HEADERS
        )

        if response.status_code != 200:
            print("[ERROR] ", response.json())
            return
        
        response_data = response.json()["data"]
        answer: str = response_data["transcript"]
        print(f"Server answer is : '{answer}'")
                
        self.lock.acquire()
        self.monitor.panel_transcript.ben_message(answer)
        self.lock.release()

        # send answer to monitor
        # listen again
        # if listen == stop : get back to listener,start()
        # else : print transpcript && send to back 
import threading
import requests
import time

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


    def run(self) -> None:
        while True:
            # wait for something to be said
            while self.transcript == "":
                self.transcript = self.listener.listen()
                if not "hey" in self.transcript:
                    self.transcript = "" # cancel tr if it don't contains activation key
            print("aaaaaaaaa")
            
            # send transcript to back end server
            self.t1 = threading.Thread(target=self._request_thread)
            self.t1.start()

            # start monitor on main loop
            self.monitor = Monitor()        
            self.monitor.start()

            # get back thread
            self.t1.join()

    
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

        if "quit" in copy_tr:
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

        # Start listening again
        print("[ INFO] Ready to listen again...")
        self._request_thread(listen=True)
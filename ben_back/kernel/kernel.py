from router.router import Router

class Kernel:
    def __init__(self):
        self.router = Router()
        
        
    def start(self) -> None:
        self.router.run()
from flask import Flask, request, jsonify

from router.router import Router
from strategy.strategy import Strategy
from strategy.strategist import Strategist
from api_orchestrator.api_orchestrator import APIOrchestrator
from DBController import DBController

class Kernel:
    def __init__(self):
        self.router = Router()
        self.router.add_endpoint('/api/ask', 'ask', self.route_ask, methods=['POST'])
        self.router.add_endpoint('/api/asnwer', 'asnwer', self.route_answer, methods=['GET'])
        self.strategist = Strategist()
        self.orchestrator = APIOrchestrator()

        
    def start(self) -> None:
        self.router.run()


    def route_ask(self):
        # Logic for POST request
        data: str = request.get_data(as_text=True) 
        strategy: Strategy = self.strategist.process_demand(data)
        print(f"[DEBUG] strategy: {strategy}")

        response: int = self.orchestrator.execute(strategy)
        print(f"[DEBUG] response: {response}")
        print("[transcript]")
        DBController.write(data, response)
        DBController.close()
        return jsonify({"message": "POST request has been received correctly", "data": response})


    def route_answer(self):
        # Logic for GET request
        return jsonify({"message": "This is a GET response."})
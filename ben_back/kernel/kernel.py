from flask import Flask, request, jsonify

from router.router import Router
from strategy.strategy import Strategy
from strategy.strategist import Strategist
from api_orchestrator.api_orchestrator import APIOrchestrator
from DBController.DBController import DBController

class Kernel:
    def __init__(self):
        self.router = Router()
        self.router.add_endpoint('/api/ask', 'ask', self.route_ask, methods=['POST'])
        self.router.add_endpoint('/api/asnwer', 'asnwer', self.route_answer, methods=['GET'])
        self.strategist = Strategist()
        self.orchestrator = APIOrchestrator()
        self.db_controller = None

        
    def start(self) -> None:
        self.router.run()


    def route_ask(self):
        # Logic for POST request
        data: str = request.get_data(as_text=True) 
        strategy: Strategy = self.strategist.process_demand(data)
        print(f"[DEBUG] strategy: {strategy}")

        response: dict = self.orchestrator.execute(strategy)
        print(f"[DEBUG] response: {response}")

        if not self.db_controller:
            self.db_controller = DBController()
        self.db_controller.write(data, response["transcript"])
        self.db_controller.close()
        return jsonify({"message": "POST request has been received correctly", "data": response})


    def route_answer(self):
        # Logic for GET request
        return jsonify({"message": "This is a GET response."})
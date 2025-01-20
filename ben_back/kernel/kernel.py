from flask import Flask, request, jsonify

from router.router import Router
from strategy.strategy import Action, Strategy

class Kernel:
    def __init__(self):
        self.router = Router()
        self.router.add_endpoint('/api/ask', 'ask', self.route_ask, methods=['POST'])
        self.router.add_endpoint('/api/asnwer', 'asnwer', self.route_answer, methods=['GET'])
        

    def route_ask(self):
        # Logic for POST request
        data: str = request.get_data(as_text=True) 

        strategy: Strategy = self.process_demand(data)
        response: int = self.execute_demand(strategy)

        return jsonify({"message": "POST request has been received correctly", "data": response})


    def route_answer(self):
        # Logic for GET request
        return jsonify({"message": "This is a GET response."})


    def process_demand(self, transcript: str) -> Strategy:
        intent: dict = self.parse_transcript(transcript)

        if intent.get("action", Action.UNKNOWN) == Action.QUIT:
            return Strategy(Action.QUIT, intent.get("data", {}))

        if intent.get("action", Action.UNKNOWN) == Action.WEATHER:
            return Strategy(Action.WEATHER, intent.get("data", {}))
        
        if intent.get("action", Action.UNKNOWN) == Action.MUSIC:
            return Strategy(Action.MUSIC, intent.get("data", {}))

        if intent.get("action", Action.UNKNOWN) == Action.EMAIL:
            return Strategy(Action.EMAIL, intent.get("data", {}))
        
        if intent.get("action", Action.UNKNOWN) == Action.SEARCH:
            return Strategy(Action.SEARCH, intent.get("data", {}))
        
        return Strategy(Action.UNKNOWN, intent.get("data", {}))
        

    def execute_demand(self, strategy: Strategy) -> dict:
        """Execute demand based on a strategy.
        Return codes:
            0  : Demand has been executed correctly
            -1 : Wtf his should not happend
            -2 : Missing data to execute command
            -3 : ... 
        """
        # TODO : call APIController with given strategy
        #   it is APIController that decider what to do depending on the strategy
        #   it will probably looks like `self.api_controller.query(strategy)`

        WTF: dict = {
            "code": -1,
            "message": "Something unexpected happened."
        }
        return WTF


    def parse_transcript(self, transcript: str) -> dict:
        result: dict = {}

        
    def start(self) -> None:
        self.router.run()
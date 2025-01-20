from flask import Flask, request, jsonify

from router.router import Router
from strategy.strategy import Strategy
from strategy.strategist import Strategist

class Kernel:
    def __init__(self):
        self.router = Router()
        self.router.add_endpoint('/api/ask', 'ask', self.route_ask, methods=['POST'])
        self.router.add_endpoint('/api/asnwer', 'asnwer', self.route_answer, methods=['GET'])
        self.strategist = Strategist()

        
    def start(self) -> None:
        self.router.run()


    def route_ask(self):
        # Logic for POST request
        data: str = request.get_data(as_text=True) 

        strategy: Strategy = self.strategist.process_demand(data)
        print(f"[DEBUG] {strategy}")
        response: int = self.execute_demand(strategy)

        return jsonify({"message": "POST request has been received correctly", "data": response})


    def route_answer(self):
        # Logic for GET request
        return jsonify({"message": "This is a GET response."})


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
        

        # DEBUG #####################
        prout: dict = {
            "code": 0,
            "transcript": "Hey! It is actually sunny in Paris, with 17 degrees celcius!"
        }
        return prout
        ############################# 

        return {
            "code": -1,
            "transcript": "Something unexpected happened."
        }
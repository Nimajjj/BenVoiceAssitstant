from flask import Flask, request, jsonify


from router.router import Router


class Kernel:
    def __init__(self):
        self.router = Router()
        self.router.add_endpoint('/api/ask', 'ask', self.route_ask, methods=['POST'])
        self.router.add_endpoint('/api/asnwer', 'asnwer', self.route_answer, methods=['GET'])
        
    def route_ask(self):
        # Logic for POST request
        data = request.get_data(as_text=True)  # Extract JSON data from the request
        return jsonify({"message": "POST request has been received correctly", "code": 200})


    def route_answer(self):
        # Logic for GET request
        return jsonify({"message": "This is a GET response."})

        
    def start(self) -> None:
        self.router.run()
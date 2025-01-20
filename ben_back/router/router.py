from flask import Flask, request, jsonify

class Router:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()


    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)


    def setup_routes(self):
        def route_answer():
            # Logic for GET request
            return jsonify({"message": "This is a GET response."})

        def route_ask():
            # Logic for POST request
            data = request.get_data(as_text=True)  # Extract JSON data from the request
            return jsonify({"message": "This is a POST response.", "data": data})

        self.add_endpoint('/api/ask', 'ask', route_ask, methods=['POST'])
        self.add_endpoint('/api/asnwer', 'asnwer', route_answer, methods=['GET'])


    def run(self, host='0.0.0.0', port=5555, debug=True):
        self.app.run(host=host, port=port, debug=debug)

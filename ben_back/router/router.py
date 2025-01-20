from flask import Flask, request, jsonify

class Router:
    def __init__(self):
        self.app = Flask(__name__)


    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)


    def run(self, host='0.0.0.0', port=5555, debug=True):
        self.app.run(host=host, port=port, debug=debug)

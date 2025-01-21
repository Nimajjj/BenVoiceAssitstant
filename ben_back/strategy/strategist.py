import requests
import json

from strategy.strategy import Action, Strategy

API_KEY = "YzsPgwgVM2sKWxnknysQuUXe3QNsw4J1" # valid until the 23/01
URL = "https://api.mistral.ai/v1/chat/completions"

class Strategist:
    def __init__(self):
        self.system_message = {
            "role": "system",
            "content": (
                "You are an intent and data extraction assistant. Analyze the user's input and "
                "respond with a JSON object following one of these templates:\n\n"
                "Templates:\n"
                "1. Weather:\n"
                "{\n  \"action\": \"weather\",\n  \"data\": {\n    \"location\": \"<location>\",\n    \"time\": \"<time>\"\n  }\n}\n\n"
                "2. Music:\n"
                "{\n  \"action\": \"music\",\n  \"data\": {\n    \"song\": \"<song>\"}\n}\n\n"
                "if no specific song is given :"
                "{\n  \"action\": \"music\",\n  \"data\": {\n    \"song\": \"random\"}\n}\n\n"
                "3. Email:\n"
                "{\n  \"action\": \"email\",\n  \"data\": {\n    \"recipient\": \"<recipient>\",\n    \"subject\": \"<subject>\",\n    \"body\": \"<body>\"\n  }\n}\n\n"
                "4. General information:\n"
                "{\n  \"action\": \"search\",\n  \"data\": {\n    \"answer\": \"<answer>\"}\n}\n\n"
                "Respond strictly using one of these templates, filling in the appropriate fields based on the input."
            )
        }



    def parse_transcript(self, transcript: str) -> dict:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        messages = [self.system_message] + [{
            "role": "user",
            "content": transcript
        }]

        payload = {
            "model": "mistral-small-latest",
            "temperature": 0.2,
            "messages": messages,
            "max_tokens": 100
        }
        response = requests.post(URL, json=payload, headers=headers)

        if response.status_code == 200:
            data: dict = json.loads(response.json()["choices"][0]["message"]["content"])
            data["action"] = Action.from_str(data["action"])
            print(f"[DEBUG] {response.json()}")
            print(f"[DEBUG] {type(data)} {data}")
            print(f"[DEBUG] {type(data["data"])} {data["data"]}")
            return data
        else:
            print(f"Error: {response.status_code}, {response.text}")
    

    def process_demand(self, transcript: str) -> Strategy:
        intent: dict = self.parse_transcript(transcript)

        if intent["action"] == Action.QUIT:
            return Strategy(Action.QUIT, intent["data"])

        if intent["action"] == Action.WEATHER:
            return Strategy(Action.WEATHER, intent["data"])
        
        if intent["action"] == Action.MUSIC:
            return Strategy(Action.MUSIC, intent["data"])

        if intent["action"] == Action.EMAIL:
            return Strategy(Action.EMAIL, intent["data"])
        
        if intent["action"] == Action.SEARCH:
            return Strategy(Action.SEARCH, intent["data"])
        
        return Strategy(Action.UNKNOWN, intent["data"])
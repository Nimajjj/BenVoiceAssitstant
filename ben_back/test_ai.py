import requests

API_KEY = "YzsPgwgVM2sKWxnknysQuUXe3QNsw4J1"
URL = "https://api.mistral.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Define the messages
messages = [
    {
        "role": "system",
        "content": (
            "You are an intent and data extraction assistant. Analyze the user's input and "
            "respond with a JSON object following one of these templates:\n\n"
            "Templates:\n"
            "1. Weather:\n"
            "{\n  \"action\": \"weather\",\n  \"data\": {\n    \"location\": \"<location>\",\n    \"time\": \"<time>\"\n  }\n}\n\n"
            "2. Music:\n"
            "{\n  \"action\": \"music\",\n  \"data\": {\n    \"song\": \"<song>\",\n    \"artist\": \"<artist>\"\n  }\n}\n\n"
            "3. Email:\n"
            "{\n  \"action\": \"email\",\n  \"data\": {\n    \"recipient\": \"<recipient>\",\n    \"subject\": \"<subject>\",\n    \"body\": \"<body>\"\n  }\n}\n\n"
            "Respond strictly using one of these templates, filling in the appropriate fields based on the input."
        )
    },
    {
        "role": "user",
        "content": "What is the weather in Paris right now?"
    }
]

payload = {
    "model": "mistral-small-latest",
    "temperature": 0.2,
    "messages": messages,
    "max_tokens": 100
}

response = requests.post(URL, json=payload, headers=headers)

if response.status_code == 200:
    print(response.json())
    print(response.json()["choices"][0]["message"]["content"])
else:
    print(f"Error: {response.status_code}, {response.text}")

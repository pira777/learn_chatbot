import requests

API_KEY = "OPENAI_API_KEY"
API_URL = "https://api.openai.com/v1/responses"

def get_ai_rely(user_message):
    headers = {
        "Authorization":f"Bearer{API_KEY}",
        "Content-Type":"application/json"
    }

    data = {
        "model":"gpt-5.4-mini",
        "input":[
            {
                "role":"system",
                "content": "You are a helpful school assistant. Answer claerly and politely"
            },

            {
                "role":"user",
                "content": user_message
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()

        # Extract response text safely
        return result["output"][0]["content"][0]["text"]

    except Exception as e:
        return "Sorry, AI service is currently unavailable."
import requests

class LectAI:
    def __init__(self, base_url=None):
        self.base_url = base_url or "https://deepseekai-api.vercel.app/chat/llama/{}"

    def get_response(self, user_prompt):
        url = f"{self.base_url}{user_prompt}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

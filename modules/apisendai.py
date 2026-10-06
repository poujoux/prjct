import openai
import requests


class sendai():
    api_base = "https://api.deepseek.com"

    def __init__(self, api_key, temp: int = 1.3, tokens: int = 700):
        openai.api_key = api_key
        openai.api_base = sendai.api_base
        self.temp = temp
        self.tokens = tokens

        if not api_key:
            raise ValueError("any api_key not provided")

    def sendmessage(self, rolecontent, usercontent) -> str:
        messages = [
                {"role": "system", "content": rolecontent},
                {"role": "user", "content": usercontent}
                ]

        print("the ai response is coming")


        response = openai.ChatCompletion.create(
            model="deepseek-chat",
            messages=messages,
            temperature=self.temp
        )

        text = response["choices"][0]["message"]["content"]
        
        return text


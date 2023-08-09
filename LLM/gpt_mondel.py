import openai
import json


class OAI:
    def __init__(self):
        try:
            with open("config.json", "r") as json_file:
                data = json.load(json_file)
        except:
            print("Unable to open JSON file.")
            exit()
        self.key = data["keys"][0]["OAI_key"]
        openai.api_key = self.key
        self.messages = []

    def get_messages(self):
        return self.messages

    def set_system_messages(self,messages):
        self.messages.append({"role": "system", "content": f"{messages}"})

    def del_system_messages(self,message_number):
        del self.messages[message_number]

    def init_message(self):
        for i in range(len(self.messages)):
            if self.messages[i]["role"] == "user":
                del self.messages[i]




    def generate_text(self,user_message):
        self.messages.append({"role": "user", "content": f"{user_message}"})
        response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=self.messages)
        return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    model = OAI()
    print(model.llm(input()))

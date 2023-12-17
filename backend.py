import openai
import os 

openai_key = os.environ.get("OPENAI_KEY")

class ChatBot:
    def __init__(self):
        openai.api_key = openai_key
    
    def get_response(self, user_input):
        response = "BOT BOT BOT"
        response = openai.completions.create(
           model = "text-davinci-003",
           prompt = user_input, 
           max_tokens = 3000,
           temperature=0.5
        ).choices[0].text
        return response
    

if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)

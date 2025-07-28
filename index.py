#importing modules for environment variables
import getpass
import os

#importing modules for LLM interaction
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

#setting evironment variable from .env file
env_vars = {}
try:
    with open(".env","r") as env_var:
        for line in env_var:
            env_vars[line.split('=')[0]] = line.split('=')[1]
except IOError:
    sys.exit("Could not open .env")

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = env_vars['GOOGLE_API_KEY']


#intiating model to interact with LLM
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

#calculator intiated
print("Calculator started:")
response = ""
while True:
    message = input("You: ")
    #close calculator if 'exit' is passed as input
    if message.lower().strip() == 'exit':
        print("Closing Calculator")
        break
    
    #if response is empty, it's because it's the first run, so we don't pass reponse
    if response == "":
        prompt = [
               SystemMessage(content="Act like a calculator evaluate the below expression, if it's anything outside of what a calulator an do, respond 'I am a calculator and can't perform the given action'. Just respond with the answer, no explanation"),
               HumanMessage(content=message),
           ]
    
    #if response is not empty, there's a response existing, so we pass it.
    else:
        prompt = [
               SystemMessage(content="Act like a calculator evaluate the below expression, if it's anything outside of what a calulator an do, respond 'I am a calculator and can't perform the given action'. Just respond with the answer, no explanation."),
               AIMessage(content=response),
               HumanMessage(content=message),
           ]
    
    response = model.invoke(prompt).content    
    print('Calculator: ',response)


exit(0)
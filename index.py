import getpass
import os

env_vars = {}
try:
    with open(".env","r") as env_var:
        for line in env_var:
            env_vars[line.split('=')[0]] = line.split('=')[1]
except IOError:
    sys.exit("Could not open .env")

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = env_vars['GOOGLE_API_KEY']

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")


model.invoke("Hello, world!")
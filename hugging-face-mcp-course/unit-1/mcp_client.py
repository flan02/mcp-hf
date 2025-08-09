# import os
from huggingface_hub import login
import os

print("Script started...")

token = os.getenv("HF_TOKEN")
print(f"Token value: {token}")  # Solo para depurar, luego podés borrarlo

login(token)

print("Logged in successfully")

# ? Run the agent
# tiny-agents run hugging-face-mcp-course/agent.json

# ? Gitbash char config
# set PYTHONIOENCODING=utf-8

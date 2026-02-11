import openai
from dotenv import load_dotenv
import os
from llm_client import LLMClient

# --- Configure LLM ---
# If using local model. Comment out if using OpenAI. Adjust file path as needed 
llm = LLMClient(
    backend="local",
    model_path= r"C:\Users\ggrai\AppData\Local\nomic.ai\GPT4All\Llama-3.2-1B-Instruct-Q4_0.gguf"
)
# If using OpenAI (comment out if using local model)
# load_dotenv()
# llm = LLMClient(
#     backend='openai",
#     api_key= os.getenv("OPENAI_API_KEY")
# )

#Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# --- Prepare conversation ---

messages = [
        {"role": "system", "content": "You are a helpful assistant with a no-nonsense attitude. Answer the user's query **once**, clearly and concisely. Do not invent additional USER lines. Do not speak entirely in capital letters"},
        {"role": "user", "content": "Hello. What should I eat for breakfast?."}
]

# --- Call LLM ---
# Note: No temperature / max token support for local model 
response = llm.chat(messages, temperature=0.7, max_tokens=30)

# Prevent local model from continuing conversation
first_reply = response.split("USER:")[0].strip()

# --- Print output --- 
print("Full response", response)


# backend/llm_client.py
from typing import List, Dict

class LLMClient:
    def __init__(self, backend="local", model_path=None, api_key=None):
        self.backend = backend
        if backend == "local":
            from gpt4all import GPT4All
            if model_path is None:
                raise ValueError("model_path must be provided for local backend")
            self.model = GPT4All(model_path)
        elif backend == "openai":
            import openai
            if api_key is None:
                raise ValueError("api_key must be provided for OpenAI backend")
            openai.api_key = api_key
            self.model = openai
        else:
            raise ValueError(f"Unsupported backend: {backend}")

    def chat(self, messages: List[Dict[str, str]],**kwargs) -> str:
        """
        messages: List of dicts like [{'role': 'system', 'content': '...'}, {'role':'user','content':'...'}]
        Returns: string response from LLM
        """
        if self.backend == "local":
            prompt = "\n".join([f"{m['role'].upper()}: {m['content']}" for m in messages])
            return self.model.generate(prompt)
        elif self.backend == "openai":
            response = self.model.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages, 
                **kwargs
            )
            return response.choices[0].message.content
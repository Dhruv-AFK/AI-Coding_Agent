import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash', contents="""
    Why are Boot.dev and FreeCodeCamp such great places to learn backend development? 
    Use one paragraph maximum.
    """,
)
print(response.text)
print(f"Prompt tokens : {response.usage_metadata.prompt_tokens_count}")
print(f"Response tokens : {response.usage_metadata.candidates_tokens_count}")
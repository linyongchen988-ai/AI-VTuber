from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

with open("prompts/persona.txt", "r", encoding="utf-8") as f:
    persona = f.read()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("=== AI VTuber ===")

while True:
    message = input("你：")

    if message.lower() == "exit":
        print("AI：掰掰！")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
{persona}

使用者：
{message}
"""
    )

    print("AI：" + response.text)
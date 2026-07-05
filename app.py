from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

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
        contents=message
    )

    print("AI：" + response.text)
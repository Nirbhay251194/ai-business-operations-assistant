from __future__ import annotations

from dotenv import load_dotenv
from google import genai
import os


class ChatAgent:

    def __init__(self) -> None:

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")

        self.client = genai.Client(api_key=api_key)

    def ask(self, dataframe_text: str, question: str) -> str:

        prompt = f"""
You are a senior business analyst.

Business Data:

{dataframe_text}

User Question:

{question}

Answer based only on the supplied data.

Provide:
- Direct answer
- Supporting reasoning
- Actionable recommendation
"""

        try:

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text

        except Exception as error:

            return f"Error: {error}"
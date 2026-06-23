import os
from typing import List
from urllib import response

from dotenv import load_dotenv
from google import genai


class LLMAgent:
    def __init__(self) -> None:
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY must be set in .env")

        self.client = genai.Client(api_key=api_key)

    def generate_recommendations(self, insights: List[str]) -> List[str]:
        prompt = self._build_prompt(insights)

        try:
            response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
    )
            return self._extract_recommendations(response.text)

        except Exception:
            try:
                response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt, )
                return self._extract_recommendations(response.text)

            except Exception:
                return [
            "Review counselor follow-up process",
            "Audit admission conversion workflow",
            "Track lead-to-admission conversion weekly",
            "Implement automated WhatsApp follow-up",
        ]

    def _build_prompt(self, insights: List[str]) -> str:
        formatted_insights = "\n".join(f"- {insight}" for insight in insights)
        return (
            "You are an experienced business operations consultant specializing in lead generation, "
            "admissions management, sales funnels, automation, and business process optimization. "
            "Review the following business insights and provide a concise list of actionable recommendations.\n\n"
            "Insights:\n"
            f"{formatted_insights}\n\n"
            "Respond with a short list of recommended actions."
        )

    def _parse_response_text(self, response) -> str:
         return response.text

    def _extract_recommendations(self, text: str) -> List[str]:
        recommendations: List[str] = []
        for line in text.splitlines():
            candidate = line.strip()
            if not candidate:
                continue
            if candidate.startswith("-") or candidate.startswith("*"):
                candidate = candidate[1:].strip()
            elif candidate[0].isdigit() and candidate.lstrip().startswith(tuple(str(i) for i in range(10))):
                candidate = candidate.lstrip("0123456789. )\t").strip()
            if candidate:
                recommendations.append(candidate)

        return recommendations

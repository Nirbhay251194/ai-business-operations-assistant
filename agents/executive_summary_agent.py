from __future__ import annotations

from typing import Dict, List

from agents.llm_agent import LLMAgent


class ExecutiveSummaryAgent:
    def __init__(self) -> None:
        self.llm_agent = LLMAgent()

    def generate_summary(
        self,
        metrics: Dict[str, float],
        insights: List[str],
    ) -> str:

        prompt = f"""
You are a senior business analyst.

Business Metrics:

Total Leads: {metrics.get('total_leads')}
Total Admissions: {metrics.get('total_admissions')}
Conversion Rate: {metrics.get('conversion_rate')}%

Insights:

{chr(10).join(insights)}

Create a professional executive summary.

Requirements:
- Maximum 150 words
- Business language
- Mention positive trends
- Mention risks
- Mention recommended management focus
- Write as a report for a business owner
"""

        try:
            response = self.llm_agent.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text

        except Exception:
            return (
                "Lead generation performance showed positive momentum. "
                "However, admission conversion performance requires attention. "
                "Management should focus on improving lead qualification, "
                "follow-up processes, and conversion optimization."
            )
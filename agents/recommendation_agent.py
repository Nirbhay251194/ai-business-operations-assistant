from __future__ import annotations

from typing import List


class RecommendationAgent:
    def __init__(self, insights: List[str]) -> None:
        self.insights = insights

    def generate_recommendations(self) -> List[str]:
        recommendations: List[str] = []

        if any("admissions declined" in insight.lower() for insight in self.insights):
            recommendations.extend(
                [
                    "Review counselor follow-up process",
                    "Audit admission conversion workflow",
                ]
            )

        if any("leads increased" in insight for insight in self.insights):
            recommendations.extend(
                [
                    "Improve lead qualification process",
                    "Analyze lead quality sources",
                ]
            )

        if any(
            "lead generation improved but admissions declined" in insight.lower()
            for insight in self.insights
        ):
            recommendations.extend(
                [
                    "Track lead-to-admission conversion weekly",
                    "Implement automated WhatsApp follow-ups",
                ]
            )

        # remove duplicates while preserving order
        seen: set[str] = set()
        unique_recommendations: List[str] = []
        for rec in recommendations:
            if rec not in seen:
                seen.add(rec)
                unique_recommendations.append(rec)

        return unique_recommendations

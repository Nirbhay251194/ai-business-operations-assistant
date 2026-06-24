class HealthScoreAgent:
    def calculate(
        self,
        total_leads: float,
        total_admissions: float,
        conversion_rate: float,
    ) -> int:

        score = 0

        # Lead Score (30 points)
        if total_leads >= 5000:
            score += 30
        elif total_leads >= 2000:
            score += 25
        elif total_leads >= 1000:
            score += 20
        else:
            score += 10

        # Conversion Score (40 points)
        if conversion_rate >= 20:
            score += 40
        elif conversion_rate >= 15:
            score += 30
        elif conversion_rate >= 10:
            score += 20
        else:
            score += 10

        # Admissions Score (30 points)
        if total_admissions >= 500:
            score += 30
        elif total_admissions >= 200:
            score += 25
        elif total_admissions >= 100:
            score += 20
        else:
            score += 10

        return min(score, 100)
from __future__ import annotations

import pandas as pd


class DataAgent:
    def __init__(
        self,
        data: pd.DataFrame,
        lead_column: str,
        admission_column: str,
    ) -> None:
        self.data = data
        self.lead_column = lead_column
        self.admission_column = admission_column

    def analyze(self) -> dict[str, float]:
        total_leads = self.data[self.lead_column].sum()
        total_admissions = self.data[self.admission_column].sum()

        conversion_rate = (
            (total_admissions / total_leads) * 100
            if total_leads != 0
            else 0.0
        )

        return {
            "total_leads": float(total_leads),
            "total_admissions": float(total_admissions),
            "conversion_rate": round(float(conversion_rate), 2),
        }
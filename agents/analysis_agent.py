from __future__ import annotations

from typing import List

import pandas as pd


class AnalysisAgent:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data.copy()

    def analyze(self) -> List[str]:
        if "Leads" not in self.data.columns or "Admissions" not in self.data.columns:
            raise ValueError("DataFrame must contain 'Leads' and 'Admissions' columns")

        if self.data.shape[0] == 0:
            return []

        leads = pd.to_numeric(self.data["Leads"], errors="coerce").fillna(0).astype(float)
        admissions = pd.to_numeric(self.data["Admissions"], errors="coerce").fillna(0).astype(float)

        first_leads = float(leads.iloc[0])
        last_leads = float(leads.iloc[-1])
        first_adm = float(admissions.iloc[0])
        last_adm = float(admissions.iloc[-1])

        insights: List[str] = []

        if last_leads > first_leads:
            insights.append(f"Leads increased from {int(first_leads)} to {int(last_leads)}")
        elif last_leads < first_leads:
            insights.append(f"Leads decreased from {int(first_leads)} to {int(last_leads)}")
        else:
            insights.append(f"Leads unchanged at {int(first_leads)}")

        if last_adm > first_adm:
            insights.append(f"Admissions increased from {int(first_adm)} to {int(last_adm)}")
        elif last_adm < first_adm:
            insights.append(f"Admissions decreased from {int(first_adm)} to {int(last_adm)}")
        else:
            insights.append(f"Admissions unchanged at {int(first_adm)}")

        if last_leads > first_leads and last_adm < first_adm:
            insights.append("Lead generation improved but admissions declined")

        return insights


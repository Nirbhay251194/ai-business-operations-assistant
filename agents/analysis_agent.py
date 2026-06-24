from __future__ import annotations

from typing import List

import pandas as pd


class AnalysisAgent:
    def __init__(
        self,
        data: pd.DataFrame,
        lead_column: str,
        admission_column: str,
    ) -> None:
        self.data = data.copy()
        self.lead_column = lead_column
        self.admission_column = admission_column

    def analyze(self) -> List[str]:

        if (
            self.lead_column not in self.data.columns
            or self.admission_column not in self.data.columns
        ):
            raise ValueError(
                f"Columns '{self.lead_column}' and '{self.admission_column}' must exist"
            )

        if self.data.shape[0] == 0:
            return []

        leads = (
            pd.to_numeric(
                self.data[self.lead_column],
                errors="coerce",
            )
            .fillna(0)
            .astype(float)
        )

        admissions = (
            pd.to_numeric(
                self.data[self.admission_column],
                errors="coerce",
            )
            .fillna(0)
            .astype(float)
        )

        first_leads = float(leads.iloc[0])
        last_leads = float(leads.iloc[-1])

        first_adm = float(admissions.iloc[0])
        last_adm = float(admissions.iloc[-1])

        insights: List[str] = []

        if last_leads > first_leads:
            insights.append(
                f"{self.lead_column} increased from {int(first_leads)} to {int(last_leads)}"
            )
        elif last_leads < first_leads:
            insights.append(
                f"{self.lead_column} decreased from {int(first_leads)} to {int(last_leads)}"
            )
        else:
            insights.append(
                f"{self.lead_column} unchanged at {int(first_leads)}"
            )

        if last_adm > first_adm:
            insights.append(
                f"{self.admission_column} increased from {int(first_adm)} to {int(last_adm)}"
            )
        elif last_adm < first_adm:
            insights.append(
                f"{self.admission_column} decreased from {int(first_adm)} to {int(last_adm)}"
            )
        else:
            insights.append(
                f"{self.admission_column} unchanged at {int(first_adm)}"
            )

        if last_leads > first_leads and last_adm < first_adm:
            insights.append(
                "Lead generation improved but conversions declined"
            )

        return insights
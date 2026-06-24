from typing import Dict
import pandas as pd


class SchemaAgent:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def detect_schema(self) -> Dict[str, str]:
        columns = [col.lower() for col in self.df.columns]

        schema = {
            "time_column": None,
            "lead_column": None,
            "admission_column": None,
        }

        for col in self.df.columns:
            lower = col.lower()

            if any(word in lower for word in [
                "month",
                "date",
                "time",
                "period"
            ]):
                schema["time_column"] = col

            if any(word in lower for word in [
                "lead",
                "inquiry",
                "enquiry",
                "prospect",
                "contact"
            ]):
                schema["lead_column"] = col

            if any(word in lower for word in [
                "admission",
                "enrollment",
                "enrolment",
                "conversion",
                "registration"
            ]):
                schema["admission_column"] = col

        return schema
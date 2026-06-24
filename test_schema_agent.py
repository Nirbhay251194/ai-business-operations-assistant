import pandas as pd

from agents.schema_agent import SchemaAgent


df = pd.DataFrame(
    {
        "Period": ["Jan", "Feb"],
        "Prospects": [100, 120],
        "Conversions": [10, 15],
    }
)

agent = SchemaAgent(df)

print(agent.detect_schema())
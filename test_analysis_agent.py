import pandas as pd

from agents.analysis_agent import AnalysisAgent


def main() -> None:
    df = pd.read_csv("data/sample_data.csv")
    agent = AnalysisAgent(df)
    insights = agent.analyze()
    for insight in insights:
        print(insight)


if __name__ == "__main__":
    main()

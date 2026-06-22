import pandas as pd

from agents.data_agent import DataAgent


def main() -> None:
    data = pd.read_csv("data/sample_data.csv")
    agent = DataAgent(data)
    results = agent.analyze()
    print(results)


if __name__ == "__main__":
    main()

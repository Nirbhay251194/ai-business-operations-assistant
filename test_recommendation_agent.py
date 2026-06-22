from agents.recommendation_agent import RecommendationAgent


def main() -> None:
    insights = [
        "Leads increased from 500 to 700",
        "Admissions decreased from 100 to 60",
        "Lead generation improved but admissions declined",
    ]

    agent = RecommendationAgent(insights)
    recommendations = agent.generate_recommendations()

    for recommendation in recommendations:
        print(recommendation)


if __name__ == "__main__":
    main()

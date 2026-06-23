from agents.llm_agent import LLMAgent

def main():
    insights = [
        "Leads increased from 500 to 700",
        "Admissions decreased from 100 to 60",
        "Lead generation improved but admissions declined",
    ]

    agent = LLMAgent()

    recommendations = agent.generate_recommendations(insights)

    print("\nAI RECOMMENDATIONS\n")

    for rec in recommendations:
        print(f"- {rec}")

if __name__ == "__main__":
    main()
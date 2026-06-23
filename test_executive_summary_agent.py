from agents.executive_summary_agent import ExecutiveSummaryAgent


def main():

    metrics = {
        "total_leads": 3000,
        "total_admissions": 390,
        "conversion_rate": 13,
    }

    insights = [
        "Leads increased from 500 to 700",
        "Admissions decreased from 100 to 60",
        "Lead generation improved but admissions declined",
    ]

    agent = ExecutiveSummaryAgent()

    summary = agent.generate_summary(
        metrics=metrics,
        insights=insights,
    )

    print("\nEXECUTIVE SUMMARY\n")
    print(summary)


if __name__ == "__main__":
    main()
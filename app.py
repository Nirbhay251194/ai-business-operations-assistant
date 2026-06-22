import pandas as pd
import plotly.express as px
from prometheus_client import metrics
import streamlit as st

from agents.analysis_agent import AnalysisAgent
from agents.data_agent import DataAgent
from agents.recommendation_agent import RecommendationAgent


def generate_executive_summary(
    metrics: dict, insights: list[str], recommendations: list[str]
) -> str:
    total_leads = int(metrics["total_leads"])
    total_admissions = int(metrics["total_admissions"])
    conversion_rate = metrics["conversion_rate"] * 100

    key_insight = insights[0] if insights else "No insights available."
    action_items = ", ".join(recommendations[:2]) if recommendations else "No recommendations."

    summary = (
        f"The organization processed {total_leads:,} leads with {total_admissions:,} admissions, "
        f"achieving a {conversion_rate:.1f}% conversion rate. "
        f"Key finding: {key_insight}. "
        f"Priority actions: {action_items}."
    )

    return summary


def generate_report(
    metrics: dict, insights: list[str], recommendations: list[str], summary: str
) -> str:
    lines = [
        "AI BUSINESS OPERATIONS ASSISTANT REPORT",
        "",
        "Section 1: KPI Metrics",
        f"- Total Leads: {int(metrics['total_leads'])}",
        f"- Total Admissions: {int(metrics['total_admissions'])}",
        f"- Conversion Rate: {metrics['conversion_rate']:.2%}",
        "",
        "Section 2: Analysis Insights",
    ]

    if insights:
        lines.extend(f"- {insight}" for insight in insights)
    else:
        lines.append("- No insights available.")

    lines.extend(["", "Section 3: Recommendations"])
    if recommendations:
        lines.extend(f"- {recommendation}" for recommendation in recommendations)
    else:
        lines.append("- No recommendations available.")

    lines.extend(["", "Section 4: Executive Summary", summary])

    return "\n".join(lines)


def main() -> None:
    st.title("AI Business Operations Assistant")

    use_sample_data = st.sidebar.checkbox("Use Sample Data", value=False)

    if use_sample_data:
        try:
            df = pd.read_csv("data/sample_data.csv")
            st.info("Loaded sample data from `data/sample_data.csv`")
        except Exception as error:
            st.error(f"Failed to load sample data: {error}")
            return
    else:
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if uploaded_file is None:
            st.info("Upload a CSV file to see KPI metrics.")
            return

        try:
            df = pd.read_csv(uploaded_file)
        except Exception as error:
            st.error(f"Failed to read CSV: {error}")
            return

    st.subheader("Data Preview")
    st.dataframe(df.head())

    try:
        data_agent = DataAgent(df)
        metrics = data_agent.analyze()
        analysis_agent = AnalysisAgent(df)
        insights = analysis_agent.analyze()
        recommendation_agent = RecommendationAgent(insights)
        recommendations = recommendation_agent.generate_recommendations()
    except Exception as error:
        st.error(f"Failed to compute metrics: {error}")
        return

    summary = generate_executive_summary(metrics, insights, recommendations)
    st.subheader("Executive Summary")
    st.info(summary)

    report_text = generate_report(metrics, insights, recommendations, summary)
    st.download_button(
        label="📥 Download Report",
        data=report_text,
        file_name="business_operations_report.txt",
        mime="text/plain",
    )

    st.subheader("Full Report")

    st.subheader("KPI Metrics")
    st.metric("Total Leads", int(metrics["total_leads"]))
    st.metric("Total Admissions", int(metrics["total_admissions"]))
    st.metric("Conversion Rate", f"{metrics['conversion_rate']:.2f}%")


    if "Leads" in df.columns and "Admissions" in df.columns:
        st.subheader("Trends")

        leads_chart = px.line(
            df,
            y="Leads",
            title="Leads Trend",
            markers=True,
        )
        st.plotly_chart(leads_chart, use_container_width=True)

        admissions_chart = px.line(
            df,
            y="Admissions",
            title="Admissions Trend",
            markers=True,
        )
        st.plotly_chart(admissions_chart, use_container_width=True)

    if insights:
        st.subheader("Analysis Insights")
        for insight in insights:
            st.write(f"- {insight}")

    if recommendations:
        st.subheader("Recommendations")
        for recommendation in recommendations:
            st.write(f"- {recommendation}")


if __name__ == "__main__":
    main()



import io

import pandas as pd
import plotly.express as px
from prometheus_client import metrics
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
import streamlit as st

from agents.analysis_agent import AnalysisAgent
from agents.data_agent import DataAgent
from agents.llm_agent import LLMAgent


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
) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontSize=24,
        textColor="#1f77b4",
        spaceAfter=12,
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor="#1f77b4",
        spaceAfter=6,
    )

    story.append(Paragraph("AI BUSINESS OPERATIONS ASSISTANT REPORT", title_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Section 1: KPI Metrics", heading_style))
    story.append(
        Paragraph(
            f"<b>Total Leads:</b> {int(metrics['total_leads']):,}",
            styles["Normal"],
        )
    )
    story.append(
        Paragraph(
            f"<b>Total Admissions:</b> {int(metrics['total_admissions']):,}",
            styles["Normal"],
        )
    )
    story.append(
        Paragraph(
            f"<b>Conversion Rate:</b> {metrics['conversion_rate']:.2%}",
            styles["Normal"],
        )
    )
    story.append(Spacer(1, 12))

    story.append(Paragraph("Section 2: Analysis Insights", heading_style))
    if insights:
        for insight in insights:
            story.append(Paragraph(f"• {insight}", styles["Normal"]))
    else:
        story.append(Paragraph("No insights available.", styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Section 3: Recommendations", heading_style))
    if recommendations:
        for recommendation in recommendations:
            story.append(Paragraph(f"• {recommendation}", styles["Normal"]))
    else:
        story.append(Paragraph("No recommendations available.", styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Section 4: Executive Summary", heading_style))
    story.append(Paragraph(summary, styles["Normal"]))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


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
        recommendation_agent = LLMAgent()
        recommendations = recommendation_agent.generate_recommendations(insights)
    except Exception as error:
        st.error(f"Failed to compute metrics: {error}")
        return

    summary = generate_executive_summary(metrics, insights, recommendations)
    st.subheader("Executive Summary")
    st.info(summary)

    report_pdf = generate_report(metrics, insights, recommendations, summary)
    st.download_button(
        label="📥 Download Report",
        data=report_pdf,
        file_name="business_operations_report.pdf",
        mime="application/pdf",
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



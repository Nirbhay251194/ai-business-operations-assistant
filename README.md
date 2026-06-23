# AI Business Operations Assistant

An AI-powered business analytics platform that transforms raw CSV business data into actionable insights, executive summaries, recommendations, and downloadable reports.

## Overview

AI Business Operations Assistant helps business owners, managers, and operations teams quickly understand business performance without manually analyzing spreadsheets.

The application combines:

* Data Analytics
* KPI Tracking
* Business Intelligence
* AI-Powered Recommendations
* Executive Reporting
* Conversational Data Analysis

Built using Python, Streamlit, Pandas, Plotly, and Google Gemini.

---

## Features

### KPI Dashboard

Automatically calculates:

* Total Leads
* Total Admissions
* Conversion Rate

### Trend Analysis

Visualizes:

* Lead Trends
* Admission Trends

using interactive Plotly charts.

### Analysis Agent

Generates business insights such as:

* Lead growth
* Admission decline
* Funnel performance trends

### AI Recommendation Agent

Uses Google Gemini to provide actionable business recommendations.

Examples:

* Improve counselor follow-up
* Optimize conversion workflow
* Increase lead qualification quality

### Executive Summary Agent

Generates management-level summaries suitable for:

* Directors
* Business Owners
* Investors
* Operations Managers

### PDF Report Generator

Creates professional downloadable reports including:

* KPI Metrics
* Business Insights
* Recommendations
* Executive Summary

### Ask Your Data Chat

Users can ask natural language questions about uploaded business data.

Examples:

* Why are admissions decreasing?
* What is the biggest risk in this dataset?
* How can conversion rates be improved?

---

## Project Architecture

```text
CSV Data
    │
    ▼
Data Agent
    │
    ▼
Analysis Agent
    │
    ▼
Recommendation Agent (Gemini)
    │
    ▼
Executive Summary Agent
    │
    ▼
Dashboard + PDF Report
    │
    ▼
Ask Your Data Chat
```

---

## Tech Stack

### Frontend

* Streamlit

### Data Processing

* Pandas

### Visualization

* Plotly

### AI

* Google Gemini API

### Reporting

* ReportLab

### Language

* Python 3.12

---

## Project Structure

```text
ai-business-operations-assistant/
│
├── agents/
│   ├── __init__.py
│   ├── data_agent.py
│   ├── analysis_agent.py
│   ├── recommendation_agent.py
│   ├── executive_summary_agent.py
│   ├── chat_agent.py
│   └── llm_agent.py
│
├── data/
│   └── sample_data.csv
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-business-operations-assistant.git
cd ai-business-operations-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Sample Dataset Format

```csv
Month,Leads,Admissions
April,500,100
May,600,90
June,550,80
July,650,60
August,700,60
```

---

## Future Enhancements

* Multi-Agent Orchestration
* Business Health Score
* Predictive Admissions Forecasting
* CRM Integration
* WhatsApp Automation
* Email Reporting
* Multi-User Authentication
* Cloud Deployment

---

## Learning Outcomes

This project demonstrates:

* Agent-Based Architecture
* Business Analytics
* LLM Integration
* Prompt Engineering
* Data Visualization
* Report Generation
* AI Product Development

---

## Author

Nirbhay Mishra

AI Generalist | Business Operations Automation | Agentic AI Builder


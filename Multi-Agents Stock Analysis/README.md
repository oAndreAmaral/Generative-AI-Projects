# Multi-Agents Stock Analysis

**Multi-Agents Stock Analysis** is a multi-agent AI system that provides stock recommendations by combining **web-based company research, financial data, and analysis agents**. The system uses **4 agents** and **2 custom tools** to produce actionable stock insights.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Agents](#agents)
* [Tools](#tools)
* [Installation](#installation)
* [Usage](#usage)

---

## Project Overview

This project allows users to **analyze a company and its stock** using a multi-agent approach:

1. **research_agent** extracts information from the internet regarding a company using a pre-made tool.
2. **summarize_agent** summarizes the information extracted by Agent 1.
3. **analist_agent** fetches financial and stock data for the company using a pre-made tool.
4. **trader_agent** combines Agent 2’s summary and Agent 3’s financial data to give a **buy, sell, or maintain recommendation**.

All data retrieval is done via **custom tools**.

---

## Agents

| Agent       | Role                                                                           |
| ----------- | ------------------------------------------------------------------------------ |
| **research_agent** | Extracts company info from the internet using Tool 1                           |
| **summarize_agent** | Summarizes the extracted company information                                   |
| **analist_agent** | Retrieves financial and stock data using Tool 2                                |
| **trader_agent** | Combines outputs from Agent 2 and Agent 3 and recommends Buy / Sell / Maintain |

---

## Tools

| Tool       | Role                                                        |
| ---------- | ----------------------------------------------------------- |
| **internet_research_tool** | Custom web scraper or API for gathering company information |
| **stock_research_tool** | Custom tool for financial and stock data retrieval          |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/oAndreAmaral/stock-analysis-4th-agent.git
cd stock-analysis-4th-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

**Dependencies:**

* CrewAI
* pandas, yfinance, numpy, requests
* Any other libraries required for your custom tools

---

## Usage

1. Configure **API keys or access** for Tool 1, Tool 2 and AI model API KEY (in this example Groq API key is being used) in the .env file as a copy of the env_template.txt.

2. In the main.py define the company name and stock name to be analysed

3. Run the system:

```bash
python main.py
```

4. Agent 4 will output **Buy, Sell, or Maintain** based on the combined analysis as well as some explanations for its decision.

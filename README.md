# Multi-Agent Research Assistant

A multi-agent AI research system built with LangChain, Mistral AI, Tavily Search, and Streamlit. The application automates web research by searching the internet, extracting content from relevant sources, generating structured research reports, and providing automated critique and feedback.

## Live Demo

🚀 https://multi-agent-research-assistant-2026.streamlit.app

## Features

* Web search using Tavily Search API
* Web content extraction using BeautifulSoup
* Agentic research workflow:

  * Search Agent
  * Reader Agent
  * Writer Chain
  * Critic Chain
* Automated research report generation
* Automated report evaluation and feedback
* Interactive Streamlit UI

## Tech Stack

* Python
* LangChain
* Mistral AI
* Tavily Search API
* BeautifulSoup
* Streamlit

## Project Architecture

```text
User Query
    ↓
Search Agent
    ↓
Reader Agent
    ↓
Writer Chain
    ↓
Critic Chain
    ↓
Final Research Report
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/lavanyack311/multi-agent-research-assistant.git
cd multi-agent-research-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Run the Application

```bash
streamlit run app.py
```

## How It Works

### Search Agent

Uses the Tavily Search API to gather relevant and recent information from the web.

### Reader Agent

Extracts detailed content from selected web pages using BeautifulSoup.

### Writer Chain

Processes the collected information and generates a structured research report containing:

* Introduction
* Key Findings
* Takeaways
* Conclusion
* sources

### Critic Chain

Reviews the generated report and provides:

* Overall Score
* Areas of Strength
* Areas for Improvement
* Final Verdict

## Example Workflow

1. User enters a research topic.
2. Search Agent gathers relevant web results.
3. Reader Agent extracts detailed content from selected sources.
4. Writer Chain generates a professional research report.
5. Critic Chain evaluates the report and provides feedback.
6. Results are displayed through the Streamlit interface.

## Repository Structure

```text
multi-agent-research-assistant/
│
├── app.py
├── agents.py
├── tools.py
├── run_pipeline.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Author

**Lavanya CK**

GitHub: https://github.com/lavanyack311

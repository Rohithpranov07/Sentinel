#  SENTINEL

<div align="center">

**Guardian of Semantic Truth**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Pathway](https://img.shields.io/badge/Powered%20by-Pathway-orange)](https://pathway.com)
[![LangGraph](https://img.shields.io/badge/Orchestrated%20by-LangGraph-green)](https://github.com/langchain-ai/langgraph)

*Agentic AI system for continuous semantic correctness monitoring*

 [Documentation](docs/) • [Architecture](docs/architecture.md) 

</div>

---

## 🎯 Overview

**SENTINEL** is an intelligent multi-agent system that solves a critical problem in modern software: **semantic correctness drift**. When specifications, contracts, or policies change, systems continue operating based on outdated assumptions—passing all tests while violating their governing documents.

SENTINEL watches your specifications 24/7 and alerts you **instantly** when system behavior drifts from documented intent.

### The Problem

```
❌ Traditional Scenario:

Day 1: Contract says "Response time < 200ms"
       Your service: 150ms ✅ Compliant

Day 2: Contract updated to "Response time < 100ms"
       Your service: Still 150ms
       Tests: ✅ Passing
       Monitoring: ✅ Green
       Reality: ❌ Violating contract (nobody knows)

Day 7: Customer complaint → Emergency fix → SLA penalty
```

### Our Solution

```
✅ With SENTINEL:

Second 0: Contract updated to "< 100ms"
Second 3: 🚨 ALERT - "Service A violates updated SLA 3.2"
          Agent reasoning: "150ms exceeds new 100ms threshold"
          Recommended action: "Alert team, review feasibility"

Result: Zero violation time, proactive response
```

---

## ✨ Key Features

- **🔴 Live Document Monitoring** - Pathway-powered streaming detects spec changes in < 3 seconds
- **🧠 Semantic Understanding** - LLM agents reason about meaning, not just syntax
- **⚡ Instant Drift Detection** - Compare intent vs. behavior in real-time
- **🤖 Five Specialized Agents** - Each with clear responsibilities and reasoning chains
- **📊 Beautiful Dashboard** - Real-time compliance status and alert management
- **🔗 Integration-Ready** - REST API for Slack, PagerDuty, Jira, etc.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│     PATHWAY STREAMING LAYER             │
│  (Google Drive • SharePoint • Local)    │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│    LANGRAPH AGENT ORCHESTRATION         │
│                                         │
│  🔍 Agent 1: Spec Ingestion            │
│  🧠 Agent 2: Intent Extraction         │
│  👁️ Agent 3: Behavior Monitor          │
│  ⚠️ Agent 4: Drift Detection            │
│  🎯 Agent 5: Action Orchestrator       │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│        SENTINEL DASHBOARD               │
│  Alerts • Analytics • Remediation       │
└─────────────────────────────────────────┘
```

**Learn more:** [Architecture Documentation](docs/architecture.md)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- OpenAI API key or Anthropic API key
- Google Drive API credentials (for document monitoring)
- 8GB RAM minimum

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/sentinel.git
cd sentinel

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run setup
python setup.py install
```

### Configuration

Edit `.env` file:

```bash
# LLM Configuration
OPENAI_API_KEY=your_openai_key_here
# OR
ANTHROPIC_API_KEY=your_anthropic_key_here

# Pathway Configuration
PATHWAY_LICENSE_KEY=your_pathway_key_here

# Google Drive (for document monitoring)
GOOGLE_DRIVE_CREDENTIALS=path/to/credentials.json
GOOGLE_DRIVE_FOLDER_ID=your_folder_id

# Monitoring
LOG_LEVEL=INFO
ALERT_WEBHOOK_URL=your_slack_webhook_url  # Optional
```

### Running SENTINEL

```bash
# Start the Pathway pipeline
python -m pipeline.pathway_connector

# In another terminal, start the dashboard
streamlit run dashboard/app.py

# Access at http://localhost:8501
```

---

## 📖 Usage Example

### 1. Set Up Document Monitoring

```python
from pipeline.pathway_connector import PathwayConnector

# Initialize connector
connector = PathwayConnector(
    gdrive_folder="your_contracts_folder_id",
    local_path="./data/contracts"
)

# Start monitoring
connector.start()
```

### 2. Deploy Agents

```python
from pipeline.orchestrator import SentinelOrchestrator

# Initialize orchestrator
orchestrator = SentinelOrchestrator()

# Deploy all agents
orchestrator.deploy_agents()

# System is now monitoring 24/7
```

### 3. View Dashboard

Navigate to `http://localhost:8501` to see:
- Real-time compliance status
- Active alerts and violations
- Contract diff viewer
- Historical analytics

---


## 🧩 Agent System

### Agent 1: Spec Ingestion 🔍
**Purpose:** Live document monitoring  
**Input:** Pathway document stream  
**Output:** Updated vector embeddings  
**Key Capability:** Instant change awareness

### Agent 2: Intent Extraction 🧠
**Purpose:** Semantic understanding  
**Input:** Document content  
**Output:** Structured requirements  
**Key Capability:** Meaning extraction (not keywords)

### Agent 3: Behavior Monitor 👁️
**Purpose:** Reality tracking  
**Input:** System logs, metrics, API responses  
**Output:** Actual behavior patterns  
**Key Capability:** What system actually does

### Agent 4: Drift Detection ⚠️
**Purpose:** Violation identification  
**Input:** Intent + Behavior  
**Output:** Violations with reasoning  
**Key Capability:** Semantic comparison

### Agent 5: Action Orchestrator 🎯
**Purpose:** Intelligent response  
**Input:** Detected violations  
**Output:** Prioritized alerts, remediation  
**Key Capability:** Actionable intelligence

---

## 📊 Project Structure

```
sentinel/
├── agents/              # Five specialized AI agents
├── config/              # Configuration and prompts
├── data/                # Sample contracts and logs
├── dashboard/           # Streamlit UI
├── docs/                # Documentation
├── pipeline/            # Pathway & LangGraph integration
├── tests/               # Test suite
└── requirements.txt     # Dependencies
```

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Live Streaming** | Pathway | Real-time document monitoring |
| **Agent Orchestration** | LangGraph | Multi-agent coordination |
| **LLM Reasoning** | Claude Sonnet 4 / GPT-4 | Semantic understanding |
| **Vector Store** | Pathway VectorStore | Embedding management |
| **Dashboard** | Streamlit | User interface |
| **Language** | Python 3.11+ | Primary development |
| **Testing** | pytest | Test framework |

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test suite
pytest tests/test_agents.py

# Run with coverage
pytest --cov=sentinel tests/

# Run integration tests
pytest tests/test_integration.py -v
```

---

## 📈 Roadmap

### Phase 1: Core (Hackathon - 11 days) ✅
- [x] Five-agent architecture
- [x] Pathway integration
- [x] Basic dashboard
- [x] Demo scenarios

### Phase 2: Production (Post-Hackathon)
- [ ] Advanced conflict resolution (multi-doc reasoning)
- [ ] Auto-remediation suggestions
- [ ] Slack/Teams/PagerDuty integrations
- [ ] Historical drift analytics

### Phase 3: Enterprise
- [ ] Multi-tenant support
- [ ] RBAC and audit logs
- [ ] Custom agent training
- [ ] Compliance report generation

---

### Development Setup

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run linters
black .
flake8 sentinel/
mypy sentinel/
```

---

## 📝 Documentation

- [Architecture Overview](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Demo Script](docs/demo_script.md)
- [Agent Design](docs/agents/)
- [Deployment Guide](docs/deployment.md)

---

## 🏆 Hackathon Info

**Track:** Agentic AI with Live Data  
**Challenge:** Build agents that never work with stale knowledge  
**Innovation:** First autonomous semantic correctness monitoring system  
**Impact:** Prevents SLA violations, compliance breaches, operational chaos

### Key Differentiators

✅ **Live** - Pathway streaming (< 3s change detection)  
✅ **Semantic** - LLM reasoning (meaning, not syntax)  
✅ **Agentic** - Multi-agent coordination (sophisticated logic)  
✅ **Autonomous** - No manual triggers (always watching)

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Pathway** - For the incredible live streaming framework
- **LangGraph** - For production-grade agent orchestration
- **Anthropic/OpenAI** - For powerful LLM reasoning capabilities


---

## 📧 Contact

**Team:** Project Sentinal AI  
**GitHub:** (https://github.com/Rohithpranov07)  
**Email:** Rohithpranov.v2024@vitstudent.ac.in


---

<div align="center">

**Built with ❤️ for the Agentic AI Hackathon**

🛡️ **SENTINEL - Guardian of Semantic Truth** 🛡️

*Change a contract. See the alert in 3 seconds.*

</div>

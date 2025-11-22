# 📑 Enterprise Workflow Agent – MultiAgent/A2A  
**Title:** Enterprise Agent – One Stop AI Assistant for Organization and Project Queries  

---

## 🚨 Problem Statement #1: Organizational Queries  
Organizations struggle to provide employees with timely access to policies, resources, and tools due to:  
- **Fragmented information delivery** – scattered across multiple platforms.  
- **Manual dependency** – HR/admin teams spend time handling repetitive requests.  
- **Inconsistent employee experience** – onboarding and daily queries are slow.  
- **Compliance risks** – delays/errors in granting access lead to regulatory issues.  
- **High operational costs** – multiple systems and teams without automation.  

**Goal:** Centralize, automate, and standardize policy/system access to improve efficiency, reduce costs, enhance employee experience, and ensure compliance.  

---

## 🚨 Problem Statement #2: Project Queries  
Project-related document access faces similar inefficiencies:  
- **Fragmented storage** – spread across email, drives, collaboration tools.  
- **Access control issues** – delays in permissions impact timelines.  
- **Lack of standardization** – inconsistent naming/versioning causes confusion.  
- **Manual dependency** – human effort required for document retrieval.  
- **Reduced productivity** – difficulty locating updated documents slows collaboration.  

**Goal:** Centralize, automate, and secure project document access to improve efficiency, compliance, and collaboration.  

---

## ⚠️ Common Issues Across Both Domains  
- Delays in providing access to policies, tools, and documents.  
- Heavy manual dependency.  
- Slower project ramp-up.  
- Compliance risks.  
- High operational costs and reduced productivity.  

---
  
## 💡 Solution: Clarity – One Stop AI Assistant  
Clarity is designed as a **multi-agent system** that intelligently routes queries to specialized agents, ensuring seamless access to organizational and project information.  

### Archiecture Diagram :

![Agent Diagram](./architecture_diagram.jpeg)


### 🧩 Clarity Agent (Client Layer)  
- Accepts raw queries from employees.  
- Prepares queries for deeper analysis.  
- Determines **nature and intent** (Organization vs Project).  
- Routes queries to specialized agents via **context-aware routing**.  

---

### 🏢 Organization Agent  
- Handles HR, payroll, compliance, and policy queries.  
- Uses **Fire Crawl MCP Server** to extract policy content from external sites.  
- **Current Scope:** Demo setup for retrieving organizational policies.  
- **Future Scope:** Integration with HR systems (API/DB) for paysheets, leave balances, etc.  

---

### 🛠️ Remote Design System Agent  
- Handles project-related queries.  
- Connects to external project agents via **A2A protocol**.  
- Example: **Carbon Design System Project Agent** for design consistency and implementation guidelines.  
- Uses **Fire Crawl MCP Server** to extract project documents from GitHub repositories.  

---

### 🔗 Remote Server Integration  
- Specialized agents hosted externally (e.g., Carbon Design System Agent).  
- Seamless communication via **Agent-to-Agent (A2A) protocol**.  
- Scalable – new project-specific agents can be spun up as needed.  

---

## 🌟 Key Benefits of Clarity Workflow  
| Benefit | Impact |
|---------|--------|
| **Context-Aware Routing** | Queries directed to the right agent automatically |
| **Resource Access** | Faster onboarding and support for employees |
| **Scalability** | Supports both organizational and project queries |
| **Remote Integration** | Access specialized knowledge bases via A2A |
| **Automation** | Reduces manual effort and operational costs |
| **Compliance** | Ensures timely and accurate access to policies/documents |

---

## 🚀 Strategic Value  
- **Efficiency Gains:** Automated query handling reduces turnaround time.  
- **Cost Reduction:** Lower manpower dependency and system overhead.  
- **Employee Experience:** Unified access point improves onboarding and daily productivity.  
- **Compliance Assurance:** Timely access reduces regulatory risks.  
- **Future-Proofing:** Scalable architecture supports new agents and integrations.

***

## Setup environment

### Prerequisites

- Python installed
- **Gemini API** key
- A **GCP Project** with:
  - **Billing enabled**
  - **Vertex AI APIs** enabled
- **FireCrawl** account and its API key (Third party tools supported by google ADK)
- [Google Application Credential Set up in Environtment variable](https://docs.cloud.google.com/docs/authentication/application-default-credentials)
---


### 1. Clone the Repository
```bash
git clone <repo_url>
cd enterprise-workflow-agent-A2A
```

### 2. Install python packages

```bash
python -m pip install -r requirements.txt
```

## Run first remote agent (carbon_design_system_agent)

### 1. Setup env file

Copy env file and update the provided variables in each

```bash
cd enterprise-workflow-agent-A2A/remote_agents
cp .env.example .env
```

### 2. Run Remote Agent

Expose the agent using uvicorn on port 8001.
```bash
cd enterprise-workflow-agent-A2A/remote_agents
uvicorn carbon_design_system_agent.agent:a2a_app --host localhost --port 8001
```

### 2. Verify Agent Card

Open URL "http://localhost:8001/.well-known/agent-card.json" in the browser.


## Run Local Agent

Now, Open another terminal.

### 1. Setup env file

Copy env file and update the provided variables in each

```bash
cd enterprise-workflow-agent-A2A/client_agent/
cp .env.example .env
```

### 2. Run Client Agent

Run it using adk web.
```bash
adk web
```

### 3. Access the agent

Open URL "http://localhost:8000" in the browser.

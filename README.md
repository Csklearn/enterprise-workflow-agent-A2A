
# Enterprise WorkFlow Agent - MultiAgent/A2A 

**Title** :  Enterprise Agent - One Stop AI assistant for organization and project related queries

**Problem Statement # 1 :**

Currently  Organizations are investing heavily in manpower and systems to provide employees with timely access to company policies, resources, and essential tools. Despite these investments, many face persistent challenges such as:

*  **Fragmented information delivery**: Policies and access details are scattered across multiple platforms, making it difficult for employees to find accurate and updated information.
* **Manual dependency**: Significant human effort is required to manage requests for policy documents, system access, and compliance checks, leading to inefficiencies and delays.
* **Inconsistent employee experience**: Lack of a unified system results in confusion, slower onboarding, and reduced productivity.
* **Compliance risks**: Delays or errors in granting access to critical systems and policies can lead to non-compliance with regulatory requirements.
* **High operational costs**: Maintaining separate teams and systems without automation increases overhead.

The organization needs to evaluate whether current investments in manpower and technology are delivering value and identify opportunities to centralize, automate, and standardize the process of providing policy information and system access. The goal is to improve efficiency, reduce costs, enhance employee experience, and ensure compliance.

**Problem Statement # 2:**

Organizations often invest in document management systems and dedicated teams to ensure employees can access project-related documents efficiently. 

However, several challenges persist:

* **Fragmented storage**: Project documents are spread across multiple platforms (email, shared drives, collaboration tools), making retrieval time-consuming.
* **Access control issues**: Employees face delays in obtaining permissions for critical documents, impacting project timelines.
* **Lack of standardization**: Inconsistent naming conventions and version control lead to confusion and errors.
* **Manual dependency**: Significant human effort is required to manage document requests and maintain repositories.
* **Reduced productivity**: Difficulty in locating accurate and updated documents slows down decision-making and collaboration.

The organization needs to assess whether current investments in manpower and systems are delivering value and identify opportunities to centralize, automate, and secure document access. The goal is to improve efficiency, ensure compliance, and enhance collaboration across teams.

**Common Issues** :

* Delay in providing access to company policies, essential tools, and project-related documents for 
   both new hires during onboarding and existing team members
* More Manual dependency.
* Slower project ramp-up.
* Compliance risks. 
* High operational costs and reduced productivity.

**Solution**:

We have created a One Stop AI assistant called **Clarity** which will assist employee about Organization policies and project documents with seamless information's.

![Agent Diagram](./architecture_diagram.jpeg)


There are 3 agents involved:

1. **AI Assistant:** This is a local  agent (Clarity) where user will communicate directly.

2. **Specialized Agents:** 
  *   **Organization Agent**:
        *   Handles organizational-level queries.
        *   Provides information on HR policies, payroll, and other administrative matters by using FireCrawl MCP server.
  *   **Remote Design System Agent**:
        *   Handles project-related queries by calling dcarbon design system project Agent which is hosted in external server through A2A protocol.
        *   Focuses on technical aspects such as development standards, testing frameworks, and design systems.
    
3. **Carbon Design System Agent:** This is the remote agent which helps in providing project related information using Firecrawl API.

---

## Prerequisites

- Python installed
- **Gemini API** key
- A **GCP Project** with:
  - **Billing enabled**
  - **Vertex AI APIs** enabled
- **FireCrawl** account and its API key (Third party tools supported by google ADK)
- [Google Application Credential Set up in Environtment variable](https://docs.cloud.google.com/docs/authentication/application-default-credentials)
---

## Setup environment

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

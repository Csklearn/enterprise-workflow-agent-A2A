
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

Here the below details of our Enterprise Agent :

![Agent Diagram](./architecture_diagram.jpeg)


**Clarity Agent (Client)**:

*   This Agent acts as the initial processing layer which will accept all user queries.
*   Its primary role is to receive raw queries and prepare them for deeper analysis.
*   It ensures that queries are structured and interpretable before moving forward.
*   At this stage, the Clarity Agent determines the **nature and intent** of the query.
*   The analysis splits queries into two major categories:
    *   **Organization Queries**: Related to company policies, payroll, HR guidelines, compliance, etc.
    *   **Project Queries**: Related to development tasks, testing procedures, design systems, and technical implementations.

**Specialized Agents**:

* Based on the context, queries are routed to appropriate agents by Clarity Agent intelligently:
    *   **Organization Agent**:
        *   Handles organizational-level queries.
        *   Provides information on HR policies, payroll, and other administrative matters.
        * **Tools**: 
            **Fire Crawl MCP Server** which will extract the content of Organization policies from external   site.
        * **Current scope** : 
               For Demo purpose , Agent is set up to retrieve content only about Organization policies.
        *  **Future scope**  
               New user tool can be created to retrieve information like paysheet , Balance leave etc., from HR               system through API or DB query.

    *   **Remote Design System Agent**:
        *   Handles project-related queries by calling design system project Agent which is hosted in external   server through A2A protocol.
        *   Focuses on technical aspects such as development standards, testing frameworks, and design systems.

**Remote Server Integration**

*   The remote server hosts specialized agents, such as:
    *   **Carbon Design System Project Agent**:
        *   Dedicated to managing and answering queries related to the Carbon Design System project.
        *   Supports design consistency and implementation guidelines across projects.
*   Communication between local remote design system agent and remote agents occurs through **A2A (Agent-to-Agent)** protocol, ensuring seamless data exchange and collaboration.
* **Tools** 
 
Here we are using **Fire Crawl MCP Server** which will extract the content of project documents hosted in github repo.
       

### **Key Benefits of This Workflow**

*   **Context-Aware Routing**: Queries are intelligently directed to the right agent based on their nature.
*   **Resource Access**: Timely resource access  for both new hires and existing employee.
*   **Scalability**: Supports both organizational and project-level queries without manual intervention.
*   **Integration with Remote Systems**: Enables access to specialized knowledge bases and tools hosted externally through A2A protocol . We can spin up more such project specific agents and provide access to employee based on their assignment.
*   **Automation**: Reduces human effort by automating query analysis and resolution.


***

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

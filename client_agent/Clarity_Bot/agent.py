from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types
from google.adk.tools import AgentTool
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
import os
from dotenv import load_dotenv
load_dotenv()

FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

remote_carbon_design_system_agent = RemoteA2aAgent(
    name="carbon_design_system_agent",
    description="A helpful assistant for Carbon Design System Project",
    agent_card=(
        f"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)


organization_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="organization_agent",
    description="A helpful assistant for TechNova Organization and Employee Handbook related queries",
    instruction="Please answer the user query from url `https://drive.google.com/file/d/1d2tFZMlaG_KkO0xNQ0ykonGIvN-vJRpx/view`",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp",
            ),
            tool_filter=["firecrawl_scrape"],
        )
    ],
)

root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='root_agent',
    description='A helpful assistant for TechNova Organization/HR policies and carbon Design System project queries.',
    instruction="""
    You are the Helpful assistant, responsible for receiving and interpreting all incoming user queries.
    Your task is to:
    1. **Normalize the query**: Clean and structure the raw input for clarity.
    2. **Determine intent**: Analyze the query to identify its nature and intent.
    3. **Classify the query** into one of two categories:
        - **Organization Query**: Related to HR policies, payroll, benefits, compliance, company guidelines.
        - **Project Query**: Related to development tasks, testing procedures, design systems, technical implementations.
    4. **Route the query** to the appropriate agent:
        - If it's an **Organization Query**, forward to the **organization_agent**.
        - If it's a **Project Query**, forward to the **remote_carbon_design_system_agent**.
        - If the query is ambiguous or unclear, request clarification from the user.
        Rules:
        - Do not answer the query yourself.
        - Do not perform any business logic or data retrieval.
        - Your sole responsibility is classification and routing.


    Output Format:
        - Return a structured response indicating the **query type** and the **target agent**.
        - If clarification is needed, ask a concise follow-up question.

    """,
    tools=[AgentTool(organization_agent)],
    sub_agents=[remote_carbon_design_system_agent],
)

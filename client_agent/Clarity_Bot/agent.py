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



remote_carbon_design_system_agent = RemoteA2aAgent(
    name="carbon_design_system_agent",
    description="A helpful assistant for Carbon Design System Project",
    agent_card=(
        f"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
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
    Greeting user with you are AI assistant respond queries related to TechNova organization policies
    and carbon design system project.
    For organization related queries please execute organization_agent.
    For Development, testing and sdlc life cycle please execute carbon_design_system_agent. 
    """,
    tools=[AgentTool(organization_agent)],
    sub_agents=[remote_carbon_design_system_agent],
)

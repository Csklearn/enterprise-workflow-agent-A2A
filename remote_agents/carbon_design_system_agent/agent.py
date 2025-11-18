from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.genai import types
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
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

root_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),    
    name="carbon_design_system_agent",
    description="A helpful assistant for Carbon design system project",
    instruction="""Please answer the user query from below urls
    https://github.com/carbon-design-system/carbon/blob/main/docs/developer-handbook.md
https://github.com/carbon-design-system/carbon/blob/main/docs/release.md
https://github.com/carbon-design-system/carbon/blob/main/docs/sprint-planning.md
https://github.com/carbon-design-system/carbon/blob/main/docs/testing.md""",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp",
            ),
            tool_filter=["firecrawl_batch_scrape"],
        )
    ],
)

a2a_app = to_a2a(root_agent, port=8001)

# agents/planner_agent.py
import asyncio
import json
from mcp import Client, aiohttp

# Using a known public MCP server for sequential thinking
MCP_SEQ_THINKING_URL = "https://glama.ai/mcp/servers/@arben-adm/mcp-sequential-thinking"

async def handle_plan(task: str) -> str:
    """
    Generates a plan for a given task by calling an MCP server.

    This function is asynchronous because it performs a network request.
    """
    print("🤖 Planner Agent: Contacting MCP server to generate a plan...")
    try:
        # The 'mcp' library uses aiohttp for async HTTP requests
        async with aiohttp.ClientSession() as session:
            client = Client(session)
            
            # This makes the actual network call to the server
            response = await client.request(
                MCP_SEQ_THINKING_URL,
                "process_thought",  # The specific tool to use on the server
                {
                    "thought": f"Break down the following user request into a detailed, step-by-step technical plan: {task}",
                    "thought_number": 1,
                    "total_thoughts": 1,
                    "next_thought_needed": False,
                    "stage": "Problem Definition"
                }
            )
            
            # The server's response is JSON, which we format for readability
            plan_data = json.loads(response)
            return f"✅ PLAN CREATED VIA MCP:\n\n{json.dumps(plan_data, indent=2)}"

    except Exception as e:
        return f"❌ PLANNER FAILED: Could not connect to the MCP server. Please check the URL and your network connection. Error: {e}"

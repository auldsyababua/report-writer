# agents/memory_agent.py
import asyncio
import json
from mcp import Client, aiohttp

# This should point to your locally running Knowledge Graph Memory server.
# See: https://github.com/modelcontextprotocol/servers/tree/main/src/memory
MCP_MEMORY_URL = "http://localhost:8082"  # Example URL

async def handle_memory_store(entity_name: str, observations: list[str]) -> str:
    """
    Stores observations about an entity in the Knowledge Graph.
    This function will create the entity if it doesn't exist.
    """
    print(f"🤖 Memory Agent: Storing info about '{entity_name}' in Knowledge Graph...")
    try:
        async with aiohttp.ClientSession() as session:
            client = Client(session)
            
            # First, try to add observations. If the entity doesn't exist, this fails.
            try:
                response = await client.request(
                    MCP_MEMORY_URL,
                    "add_observations",
                    {"observations": [{"entityName": entity_name, "contents": observations}]}
                )
            except Exception:
                # If it failed, the entity likely doesn't exist. Create it.
                print(f"Entity '{entity_name}' not found. Creating it...")
                await client.request(
                    MCP_MEMORY_URL,
                    "create_entities",
                    {"entities": [{
                        "name": entity_name,
                        "entityType": "general", # Or derive from task
                        "observations": observations
                    }]}
                )
            
            return f"✅ MEMORY STORED: Successfully saved observations for '{entity_name}'."

    except Exception as e:
        return f"❌ MEMORY FAILED: Could not connect to the Knowledge Graph MCP on {MCP_MEMORY_URL}. Is it running? Error: {e}"

async def handle_memory_recall(query: str) -> str:
    """
    Searches the Knowledge Graph for a given query.
    """
    print(f"🤖 Memory Agent: Recalling info for query '{query}' from Knowledge Graph...")
    try:
        async with aiohttp.ClientSession() as session:
            client = Client(session)
            
            response = await client.request(
                MCP_MEMORY_URL,
                "search_nodes",
                {"query": query}
            )
            
            nodes = json.loads(response)
            if not nodes:
                return f"✅ MEMORY RECALLED: No information found for '{query}'."

            return f"✅ MEMORY RECALLED:\n\n{json.dumps(nodes, indent=2)}"

    except Exception as e:
        return f"❌ MEMORY FAILED: Could not connect to the Knowledge Graph MCP on {MCP_MEMORY_URL}. Is it running? Error: {e}"

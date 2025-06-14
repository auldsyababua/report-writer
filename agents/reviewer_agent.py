# agents/reviewer_agent.py
import asyncio
import json
from mcp import Client, aiohttp

# This agent reads files to perform its review.
MCP_FILESYSTEM_URL = "http://localhost:8080"

async def handle_review(file_to_review: str) -> str:
    """
    Reads a file using the Filesystem MCP and provides a simulated review.
    """
    print(f"🤖 Reviewer Agent: Reading '{file_to_review}' to perform review...")
    
    file_content = ""
    try:
        async with aiohttp.ClientSession() as session:
            client = Client(session)
            
            read_response = await client.request(
                MCP_FILESYSTEM_URL,
                "readFile",
                {"path": file_to_review}
            )
            read_result = json.loads(read_response)
            
            if not read_result.get("success"):
                return f"❌ REVIEWER FAILED: Could not read file. Error: {read_result.get('error')}"
            
            file_content = read_result.get("content", "")

    except Exception as e:
        return f"❌ REVIEWER FAILED: Could not connect to Filesystem MCP. Error: {e}"

    # In a real implementation, this prompt and the file_content would be
    # sent to an LLM for a detailed code review.
    review_prompt = f"""
    Review the following code for quality, clarity, and correctness.
    
    Code:
    ---
    {file_content}
    ---
    """
    
    simulated_review = "Looks good. The code is clean and the logic is sound. Approved."
    
    return f"✅ REVIEW COMPLETE:\n\n{simulated_review}"
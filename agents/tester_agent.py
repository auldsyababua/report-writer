# agents/tester_agent.py
import asyncio
import json
from mcp import Client, aiohttp

# This agent now uses the ForeverVM server for a persistent REPL.
# See: https://github.com/jamsocket/forevervm/tree/main/javascript/mcp-server
MCP_FOREVER_VM_URL = "http://localhost:8083" # Example URL

async def handle_test(task_description: str) -> str:
    """
    Performs interactive testing using a persistent Python REPL from ForeverVM.
    
    NOTE: Requires a ForeverVM MCP server to be running locally.
    """
    print("🤖 Tester Agent: Starting interactive test session with ForeverVM...")
    
    # Simulate the test code we want to run
    file_to_test = "generated_code.py" # Assumes coder agent created this
    test_code_import = f"import {file_to_test.replace('.py', '')}"
    test_function_call = f"{file_to_test.replace('.py', '')}.hello_world()"

    repl_id = None
    full_output = []

    try:
        async with aiohttp.ClientSession() as session:
            client = Client(session)
            
            # Step 1: Create a new Python REPL session
            print("Step 1: Creating Python REPL...")
            response = await client.request(MCP_FOREVER_VM_URL, "create-python-repl", {})
            result = json.loads(response)
            repl_id = result.get("id")
            if not repl_id:
                return f"❌ TESTER FAILED: Could not create REPL. Response: {result}"
            full_output.append(f"REPL Created with ID: {repl_id}")
            
            # Step 2: Import the generated code into the REPL
            print(f"Step 2: Importing '{file_to_test}' into REPL...")
            response = await client.request(
                MCP_FOREVER_VM_URL,
                "run-python-in-repl",
                {"replId": repl_id, "code": test_code_import}
            )
            result = json.loads(response)
            full_output.append(f"Import Result: {result.get('result')}")

            # Step 3: Execute a function from the code
            print(f"Step 3: Executing '{test_function_call}'...")
            response = await client.request(
                MCP_FOREVER_VM_URL,
                "run-python-in-repl",
                {"replId": repl_id, "code": test_function_call}
            )
            result = json.loads(response)
            full_output.append(f"Execution Result: {result.get('result')}")

            return f"✅ INTERACTIVE TEST COMPLETE:\n\n" + "\n".join(full_output)

    except Exception as e:
        return f"❌ TESTER FAILED: Could not connect to the ForeverVM MCP on {MCP_FOREVER_VM_URL}. Is it running? Error: {e}"

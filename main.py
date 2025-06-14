# main.py
import asyncio
from agents.router_agent import route_task

async def main():
    """
    The main asynchronous entry point for the agent CLI.
    """
    print("\n🧠 Agent Orchestrator CLI (Async Version)")
    print("-----------------------------------------")

    while True:
        print("\nAvailable commands:")
        print("  plan <task>   → Generate spec/blueprint for the task.")
        print("  code <plan>   → Implement functions from the plan.")
        print("  test <desc>   → Generate and run unit tests.")
        print("  review <file> → Audit a specific file.")
        print("  quit          → Exit the CLI.\n")

        user_input = input("Enter command and arguments: ").strip()
        
        if not user_input:
            continue
            
        parts = user_input.split(' ', 1)
        cmd = parts[0].lower()
        task = parts[1] if len(parts) > 1 else ""

        if cmd in {"quit", "exit"}:
            print("Exiting...")
            break
        elif cmd in {"plan", "code", "test", "review"}:
            # Await the result from our async router
            result = await route_task(cmd, task)
            print(f"\n{result}\n")
        else:
            print(f"❌ Invalid command: '{cmd}'")

if __name__ == "__main__":
    # This is the correct way to run the top-level async main function
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nCLI interrupted by user. Exiting.")

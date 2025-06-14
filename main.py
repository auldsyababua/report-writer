# main.py
import asyncio
from agents.router_agent import route_task

async def main():
    """
    The main asynchronous entry point for the agent CLI.
    """
    print("\n🧠 Agent Orchestrator CLI (With Memory)")
    print("-----------------------------------------")

    while True:
        print("\nAvailable commands:")
        print("  plan <task>                   → Generate spec for the task (uses memory).")
        print("  code <plan>                   → Implement functions from the plan.")
        print("  test <desc>                   → Run interactive tests via ForeverVM.")
        print("  review <file>                 → Audit a specific file.")
        print("  memory store entity:<name> observation:<obs1,obs2>")
        print("                                → Store information in the knowledge graph.")
        print("  memory recall <query>         → Recall information from the knowledge graph.")
        print("  quit                          → Exit the CLI.\n")

        user_input = input("Enter command and arguments: ").strip()
        
        if not user_input:
            continue
            
        parts = user_input.split(' ', 1)
        cmd = parts[0].lower()
        task = parts[1] if len(parts) > 1 else ""

        if cmd in {"quit", "exit"}:
            print("Exiting...")
            break
        elif cmd in {"plan", "code", "test", "review", "memory"}:
            # Await the result from our async router
            result = await route_task(cmd, task)
            print(f"\n{result}\n")
        else:
            print(f"❌ Invalid command: '{cmd}'")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nCLI interrupted by user. Exiting.")

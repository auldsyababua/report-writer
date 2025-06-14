# agents/router_agent.py
import asyncio
from agents.planner_agent import handle_plan
from agents.coder_agent import handle_code
from agents.tester_agent import handle_test
from agents.reviewer_agent import handle_review
from agents.memory_agent import handle_memory_store, handle_memory_recall

async def route_task(cmd: str, task: str):
    """
    Routes the user's command to the appropriate asynchronous agent handler.
    """
    print(f"\n📦 ROUTING to agent for command: {cmd}")

    if cmd == "plan":
        return await handle_plan(task)
    elif cmd == "code":
        return await handle_code(task)
    elif cmd == "test":
        return await handle_test(task)
    elif cmd == "review":
        return await handle_review(task)
    elif cmd == "memory":
        # Handle memory sub-commands, e.g., "memory store <data>" or "memory recall <query>"
        parts = task.split(' ', 1)
        sub_cmd = parts[0].lower()
        content = parts[1] if len(parts) > 1 else ""
        
        if sub_cmd == "store":
            # A simple way to parse entity and observation from string
            # e.g., "memory store entity:colin observation:likes_dogs"
            try:
                entity_parts = content.split(" observation:")
                entity_name = entity_parts[0].replace("entity:", "").strip()
                observations = [obs.strip() for obs in entity_parts[1].split(',')]
                return await handle_memory_store(entity_name, observations)
            except IndexError:
                return "❌ Invalid 'memory store' format. Use: entity:<name> observation:<obs1,obs2>"
        elif sub_cmd == "recall":
            return await handle_memory_recall(content)
        else:
            return "❌ Invalid memory command. Use 'store' or 'recall'."
    else:
        return "❌ Unknown command."

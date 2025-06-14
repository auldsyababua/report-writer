# agents/router_agent.py
import asyncio
from agents.planner_agent import handle_plan
from agents.coder_agent import handle_code
from agents.tester_agent import handle_test
from agents.reviewer_agent import handle_review
from agents.data_fetcher_agent import handle_data_fetch
from agents.notifier_agent import handle_notify

async def route_task(cmd: str, task: str):
    """
    Routes the user's command to the appropriate asynchronous agent handler.
    """
    print(f"\n📦 ROUTING to agent for command: {cmd}")

    if cmd == "plan":
        return await handle_plan(task)
    elif cmd == "code":
        # The 'handle_code' agent needs the output of the 'plan' agent.
        # For this simple template, we pass the user's task string,
        # but a real app would pass the structured plan.
        return await handle_code(task)
    elif cmd == "test":
        return await handle_test(task)
    elif cmd == "review":
        # The reviewer needs to know which file to review.
        return await handle_review(task)
    else:
        return "❌ Unknown command. Please use: plan, code, test, or review."

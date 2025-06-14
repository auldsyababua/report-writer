from agents.planner_agent import handle_plan
from agents.coder_agent import handle_code
from agents.tester_agent import handle_test
from agents.reviewer_agent import handle_review

def route_task(task: str):
    print(f"\n📦 ROUTING TASK: {task}")

    if "plan" in task.lower():
        return handle_plan(task)
    elif "code" in task.lower():
        return handle_code(task)
    elif "test" in task.lower():
        return handle_test(task)
    elif "review" in task.lower():
        return handle_review(task)
    else:
        return "❌ Unknown task type. Please include: plan, code, test, or review."

def handle_plan(task: str) -> str:
    plan = {
        "task": task,
        "modules": [
            {
                "name": "fetch_metrics",
                "description": "Collects key data points needed for the report (revenue, uptime, etc).",
                "inputs": [],
                "outputs": ["dict of metrics"]
            },
            {
                "name": "render_report",
                "description": "Loads a text template and fills in metric values.",
                "inputs": ["template_name", "metrics dict"],
                "outputs": ["report string"]
            },
            {
                "name": "send_report",
                "description": "Sends the report via Telegram using chat_id and bot_token.",
                "inputs": ["chat_id", "message_text", "bot_token"],
                "outputs": ["status code"]
            }
        ],
        "edge_cases": [
            "Missing or invalid template name",
            "Empty metrics dict",
            "Telegram API failure or invalid token"
        ]
    }

    return f"✅ PLAN CREATED:\n\n{task}\n\nModules:\n" + "\n".join(
        [f"- {m['name']}: {m['description']}" for m in plan["modules"]]
    ) + "\n\nEdge Cases:\n" + "\n".join(f"- {e}" for e in plan["edge_cases"])

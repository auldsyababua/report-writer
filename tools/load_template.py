import os

def load_template(template_name: str) -> str:
    path = os.path.join("templates", f"{template_name}_template.txt")
    if not os.path.exists(path):
        raise FileNotFoundError(f"No template found at {path}")
    with open(path, "r") as f:
        return f.read()

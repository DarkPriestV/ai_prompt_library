import json
import os

FILE = "prompts.json"

def load_prompts():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_prompt(prompt_data):
    data = load_prompts()
    data.append(prompt_data)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
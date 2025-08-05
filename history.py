import json
import os
from datetime import datetime

HISTORY_PATH = "data/history.json"

def save_to_history(image_name, detected_objects, description, keywords):
    entry = {
        "image": image_name,
        "timestamp": datetime.now().isoformat(),
        "objects": detected_objects,
        "description": description,
        "keywords": keywords,
    }

    try:
        with open(HISTORY_PATH, "r") as f:
            history = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        history = []

    history.append(entry)

    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, indent=4)


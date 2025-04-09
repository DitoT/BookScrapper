import json
import os


def save_data(data, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"ERROR: Failed to save data -> {e}")


def load_data(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found")

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to load data -> {e}")
        return None

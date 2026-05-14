from datetime import datetime

LOG_FILE = "cybershell.log"

def log_action(action):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{now}] {action}\n")

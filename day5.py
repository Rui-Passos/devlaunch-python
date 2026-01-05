import random
from datetime import datetime

STATUSES = ["UP", "DOWN"]
SERVICES = ["payments", "auth", "db", "api"]


def log_service_status(service, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("status.log", "a") as file:
        file.write(f"[{timestamp} {service}: {status}\n")


# --- Generate random status and log ---
for service in SERVICES:
    status = random.choice(STATUSES)
    log_service_status(service, status)


# --- Read logs ---
print("=== SERVICE STATUS LOG ===")

with open("status.log", "r") as file:
    for line in file:
        print(line.strip())

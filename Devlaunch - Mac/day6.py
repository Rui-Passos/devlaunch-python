# --- Error handling with try/except ---
# try:
#    age = int(input("Enter your age: "))
#    print(f"In 10 years you will be {age + 10} years old.")
# except ValueError:
#    print("Error: Please enter a valid number.")


import random
from datetime import datetime

SERVICES = ["payment", "auth", "db", "api"]
STATUSES = ["UP", "DOWN"]

def log_service_status(service, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("status.log", "a") as file:
        file.write(f"[{timestamp}] - {service}: {status}\n")

for service in SERVICES:
    try:
        status = random.choice(STATUSES)
        log_service_status(service, status)
        print(f"{service} logged as {status}")
    except Exception as e:
        print(f"Error loggin {service}: {e}")

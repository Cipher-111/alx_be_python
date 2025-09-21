# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        base = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base = f"Note: '{task}' is a low priority task"
    case _:
        base = f"Reminder: '{task}' has an unknown priority level"

if time_bound == "yes":
    message = base + " that requires immediate attention today!"
else:
    if priority == "low":
        message = base + ". Consider completing it when you have free time."
    else:
        message = base + "."

print(message)

# Prompt for a single task
task = input("Enter your task for today: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Process the task based on priority using match case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

# Add time-sensitive message if necessary
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the final customized reminder
print(reminder)

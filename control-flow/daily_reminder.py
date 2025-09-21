#take user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

#check priority of task
match priority:
    case "high" | 'h':
        message = "high"
    case "medium" | 'm':
        message = "medium"
    case "low" | 'l':
        message = "low"

if time_bound == "yes" or 'y' and message == "high":
    print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
else:
    print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
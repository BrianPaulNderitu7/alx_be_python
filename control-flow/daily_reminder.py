# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
print("Reminder: ", end="")
match priority:
    case "high":
        print(f"'{task}' is a high priority task", end="")
    case "medium":
        print(f"'{task}' is a medium priority task", end="")
    case "low":
        print(f"'{task}' is a low priority task", end="")

if time_bound == "yes":
    print(" that requires immediate attention today!")
else:
    print(". Consider completing it when you have free time.")
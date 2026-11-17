def show_warning(username, failed_attempts):
    print("Warning Too Many Failed Attempts from:", username, failed_attempts)

# Collect user information
username = input("Enter username: ")

# Security Monitoring Program [Simulated]
login_events = ["Failed", "Failed", "Failed", "Failed", "Failed"]

success_attempts = 0
failed_attempts = 0

for event in login_events:

    if event == "Failed":
        failed_attempts += 1

    else:
        success_attempts += 1

# Display monitoring results
print("Total Success Attempts:", success_attempts)
print("Total Failed Attempts:", failed_attempts)

# Display account information
print("Monitoring account:", username)

# Condition for investigation

if failed_attempts >= 5:
    show_warning(username, failed_attempts)





    

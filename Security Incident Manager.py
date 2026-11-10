# Security Incident Manager using a Dictionary function
# this program stores and updates information about a security incident.

# Create a dictionary containing security incident details
incident = {
    "username": "a.ashraf",
    "ip_address": "192.168.1.50",
    "event_type": "Failed Login",
    "risk_level": "High"
}

# Display the username and IP of the Incident
print("Username:", incident["username"])
print("IP Address:", incident["ip_address"])

# Add a new field called status
incident["status"] = "Open"

print("\nStatus has been added.")

# Update the risk level of the incident   
incident["risk_level"] = "Critical"

print("Risk level updated to:", incident["risk_level"])

# Remove one field from the dictionary and print that it has been removed
del incident["event_type"]

print("Event type has been removed.")

# Display all remaining keys and values
print("\nRemaining Security Incident Details:")

for key, value in incident.items():
    print(key, ":", value)

# Display and print all keys to the user
print("\nKeys:")
print(incident.keys())

# Display all values to the user
print("\nValues:")
print(incident.values())

# Display the total number of key-value pairs to the user
print("\nTotal key-value pairs:", len(incident))

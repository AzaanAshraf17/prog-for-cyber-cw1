# Import required modules for the Event logger to work properly 
import random
from datetime import datetime
import socket

# Correct login details for the Security event logger program
correct_username = "admin"
correct_password = "Password1722!!"

# Gets the IP address of the system you are currently using 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
s.close()

print("SECURITY EVENT LOGGER")
print("==================")

# while loop will Keep asking until the usr entters correct username and password 
while True:

    # Ask the usr  for login details
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Generate a random 4-digit Event ID
    event_id = random.randint(1000, 9999)

    # will Get the current date and time so that the program can log the time of the event
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check whether login details are correct with the ones mentioned at the start of the program  
    if username == correct_username and password == correct_password:

        # print the findings and sucessful login details and access granted message shown  
        print("\nEvent ID:", event_id)
        print("Username:", username)
        print("IP Address:", ip_address)
        print("Event: Successful login")
        print("Timestamp:", timestamp)
        print("Access granted to event logger")
 
        # Exit the loop
        break

    else:

        # print the findings and failed login details and access denied message shown 
        print("\nEvent ID:", event_id)
        print("Username:", username)
        print("IP Address:", ip_address)
        print("Event: Failed login")
        print("Timestamp:", timestamp)
        print("Access denied to event logger please try again")

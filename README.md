# prog-for-cyber-cw1
Security Event Logger
-

student details Name: Azaan Ashraf Banner ID: B01860586 the campus I go to is UWS Lanarkshire Campus .
-

Description of the Program and how the program works
-

This program is the Security Event logger it simulates a logger system that records login attempts 

This program requires the user to log in using a stored username and password that being (admin) and (Password1722!!) after being granted access every login attempt made on the system will be recorded with a unique random Event ID , timestamped, username, IP address and event status either a successful event status or a failed event status.

the program imports the necessary python modules:

Random - Generates the Event ID
Datetime - Records Timestamps
socket - for obtaining the users IP address

if the login fails from incorrect credentials being entered it logs and records the failed security event and displays alongside it the Event ID, Username , IP , Timestamp and event type are displayed to the user it will also ask the user to try enter the right username and password again.

If the login is successful the program will record and log the security event and will allow the user access to the Security Event logger.

the file used is Security Event Logger.py
-

How to Run this Program using VScode
-
Step 1 - download the file 
-
Step 2 - Open the File on your Computer
-
Step 3 - Open the terminal of VScode
-
Step 4 - Navigate to where you have saved the program in your files
-
Step 5 - Run the file
-

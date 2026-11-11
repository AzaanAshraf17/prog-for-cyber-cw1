#import the Security tools moodule
import security_tools

print("Welcome to the CYBER SECURITY UTILITIES PROGRAM")
print ("================================")

#Ask the user to enter a password
password =input("Please enter a password and make sure the password is atleast 8 characters long or more: ")

#Check if the password the user entered is valid
if security_tools.validate_password(password):
    print("The user's password is valid and strong enough")

else:
    print("The user's password is invalid and is not strong enough")

#Suggest a strong password for the user to use
    strong_password = security_tools.generate_strong_password()

    print("Here is a Stronger password you can use:", strong_password)

#Ask the user to enter a valid IP address
ip_address =input("Please enter a valid IP address: ")

#Check to see if the IP enterted by the user is a valid address
if security_tools.validate_ip_address(ip_address):
    print("Your IP address is valid")

else:
    print("Your IP address is invalid")
